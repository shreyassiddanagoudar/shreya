"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import json
from string import Template

from examsystemapp.models.inward_draft import InwardDraftModel
from examsystemapp.models.notification.notification_default_recipients import NotificationDefaultRecipientsModel
from examsystemapp.services.notification.base_notification_service import BaseNotificationService
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.services.user_service import UserService
import os


class NotificationService(BaseNotificationService):

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        BaseNotificationService.__init__(self, ext_params, is_transaction_owner, event_type)

    def _object_type(self):
        return "EOD"

    def _get_payload(self, action, data):
        return None

    def _get_url(self, action, data):
        return None

    def _get_object_id(self, action, data):
        return None

    def _build_title(self, action, data, template, conf):
        return template

    def _build_description(self, action, data, template, conf):
        params = ParamsObject()
        params.set_params_list([])
        if conf == "COLLECTION":
            sw = 0
            ne = 0
            """ Get Data """
            collection = self.get_direct("sNotificationEODCollection", params, False)

            if collection is None:
                template = "No Collection"
            else:
                if isinstance(collection, list):
                    if len(collection) > 0:
                        for each_collection in collection:
                            if each_collection["Zone_ID"] == 1:
                                sw = each_collection["Total"]
                            else:
                                ne = each_collection["Total"]
                        template = template.replace("<TOTAL>", str(sw + ne) + os.linesep)
                        template = template.replace("<NE_QTY>", str(ne) + os.linesep)
                        template = template.replace("<SW_QTY>", str(sw) + os.linesep)
                    else:
                        template = "No Collection"
                else:
                    template = "No Collection"
        elif conf == "ALLOCATION":
            allocation = self.get_direct("sNotificationEODAllocation", params, False)

            if allocation is None:
                template = "No Allocation"
            else:
                if isinstance(allocation, list):
                    if len(allocation) > 0:
                        CONST_NAME = template
                        template_list = []
                        for each_allocation in allocation:
                            brand = each_allocation["Entity_Name"]
                            item = each_allocation["Category_Name"]
                            quantity = each_allocation["Total"]
                            temp = CONST_NAME
                            temp = temp.replace("<BRAND>", brand)
                            temp = temp.replace("<ITEM>", item)
                            temp = temp.replace("<QTY>", str(quantity))
                            template_list.append(temp + os.linesep)
                        list_to_str = ''.join(map(str, template_list))
                        template = list_to_str
                    else:
                        template = "No Allocation"
                else:
                    template = "No Allocation"
        else:
            recycle = self.get_direct("sNotificationEODRecycled", params, False)

            if recycle is None:
                template = "No Recycle"
            else:
                if isinstance(recycle, list):
                    if len(recycle) > 0:
                        template_list = []
                        CONST_NAME = template
                        for each_recycler in recycle:
                            brand = each_recycler["Entity_Name"]
                            item = each_recycler["Category_Name"]
                            quantity = each_recycler["Total"]
                            temp = CONST_NAME
                            temp = temp.replace("<RECYCLER>", brand)
                            temp = temp.replace("<ITEM>", item)
                            temp = temp.replace("<QTY>", str(quantity))
                            template_list.append(temp + os.linesep)
                        list_to_str = ''.join(map(str, template_list))
                        template = list_to_str
                    else:
                        template = "No Recycle"
                else:
                    template = "No Recycle"
        return template

    def _get_recipients(self, data, conf):
        user_device_list = []
        return user_device_list
