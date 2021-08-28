"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import json
import re

from django.http import HttpRequest, HttpResponse

from examsystemapp.services.file_service import FileService
from examsystemapp.utils.constants.constants import ErrorCodes
from examsystemapp.utils.helpers.general_helper import *
from examsystemapp.api.base_controller import BaseController
from examsystemapp.utils.exception_handling.exception import FileUploadException, KaroException
from examsystemapp.utils.helpers.file_helper import FileHelper as FileUtil
from examsystemapp.utils.helpers.ocr_helper import OCRHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject
from fuzzywuzzy import fuzz
from examsystemapp.utils.helpers.general_helper import StringHelper
from examsystemapp.services.notification.sellar_poe_notification_service import SellarPoeNotificationService
from examsystemapp.services.notification.recycler_poe_notification_service import RecyclerPoeNotificationService


class FileHelper(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    # def check_session(self, request):
    #     pass

    def upload(self, request: HttpRequest):
        draft_object = FileUtil().upload(request)
        return self.send_response_raw_json(draft_object)

    def delete(self, request: HttpRequest):
        file_object = request.POST.get("file")
        delete_by = request.POST.get("user_id")
        draft_object = FileUtil().delete(file_object, delete_by)
        return self.send_response_raw_json(draft_object)

    def get(self, request: HttpRequest):
        data = FileUtil().get_files(request.GET.get("transaction_id", ''), request.GET.get("object_type", ''),
                                    request.GET.get("document_type", ''), request.GET.get("object_id", ''),
                                    request.GET.get("document_id", ''))

        # return self.send_response_raw_json(data)
        return self.send_response_raw_json(data)

    def get_list(self, request: HttpRequest):
        data = FileUtil().get_files_multiple(request.GET.get("transaction_id", ''), request.GET.get("object_type", ''),
                                             request.GET.get("document_type", ''), request.GET.get("object_id", ''),
                                             request.GET.get("document_id", ''))

        # return self.send_response_raw_json(data)
        return self.send_response_raw_json(data)

    def get_object_list(self, request: HttpRequest):
        data = FileUtil().get_object_list()
        return self.send_response_raw_json(data)

    def get_document_list(self, request: HttpRequest):
        data = FileUtil().get_document_list()
        return self.send_response_raw_json(data)

    def get_object_document_list(self, request: HttpRequest):
        data = FileUtil().get_object_document_list()
        return self.send_response_raw_json(data)

    def get_object_document_list_multiple(self, request: HttpRequest):
        data = FileUtil().get_object_document_list_multiple(request.GET.get("object_type", ''))
        return self.send_response_raw_json(data)

    def get_files_multiple_transaction(self, request: HttpRequest):
        data = FileUtil().get_files_multiple_transaction(request.GET.get("trans_ids"), request.GET.get("object_type"))
        return self.send_response_raw_json(data)

    def get_object_document_access(self, request: HttpRequest):
        role_ids = []
        roles = self.get_roles()

        if roles != '' and roles is not None:
            for roles_dict in roles:
                role_ids.append(roles_dict['role_id'])

        if len(role_ids) <= 0:
            return self.send_response_raw_json(None)
        else:
            data = FileUtil().get_object_document_access(request.GET.get("object_document_id", ''), role_ids)
            return self.send_response_raw_json(data)

    def commit(self, request: HttpRequest):
        """
        :param files: List of file object (Draft object), which was sent by the Asset server while uploading
        :param transaction_id: Object Id
        :param transaction_type: Type of transaction/Master
        :param object: Type of object
        :param context: On what context file is being uploaded into the system
        :return: List of uploaded files
        """

        """
        {
            "transaction_id": 1,
            "created_by": 1,
            "data_object": "",
            "files": [
                {
                    "draft_id": 1
                },
                {
                    "draft_id": 2
                }
            ]
        }
        
        """

        file_json = json.loads(request.POST.get("file_json"))

        try:
            response = FileUtil().commit(file_json.get('files'), int(file_json.get('transaction_id')),
                                         file_json.get('created_by'),
                                         file_json.get('data_object'))
            return self.send_response_raw_json(response)
        except FileUploadException as ex:
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex:
            raise KaroException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def commit_all(self, request: HttpRequest):
        """
        :param files: List of file object (Draft object), which was sent by the Asset server while uploading
        :param transaction_id: Object Id
        :param transaction_type: Type of transaction/Master
        :param object: Type of object
        :param context: On what context file is being uploaded into the system
        :return: List of uploaded files
        """

        """
            {
              "created_by": 1,
              "file_detail": [
                {
                  "transaction_id": 1,
                  "data_object": "",
                  "files": [
                    {
                      "draft_id": 1
                    },
                    {
                      "draft_id": 2
                    }
                  ]
                },
                {
                  "transaction_id": 1,
                  "data_object": "",
                  "files": [
                    {
                      "draft_id": 4
                    },
                    {
                      "draft_id": 5
                    },
                    {
                      "draft_id": 6
                    },
                    {
                      "draft_id": 7
                    }
                  ]
                }
              ]
            }
        """

        file_json = json.loads(request.POST.get("file_json"))
        ext_params = self.get_entity_user_ext_params()

        try:
            response = FileUtil().commit_all(file_json.get("file_detail"), file_json.get('created_by'))
            # object_type = []
            # for i in file_json["file_detail"]:
            #     a = i
            #     for j in i["files"]:
            #         b = object_type.append(j["object_type"])
            # if object_type[0] == "SELLERINV":
            #     sellar_poe_notification_service:SellarPoeNotificationService = SellarPoeNotificationService(ext_params)
            #     sellar_poe_notification_service.send_notification("ADD",file_json)
            # elif object_type[0] == "KAROINV":
            #     recycler_poe_notification_service:RecyclerPoeNotificationService = RecyclerPoeNotificationService(ext_params)
            #     recycler_poe_notification_service.send_notification("ADD",file_json)
            return self.send_response_raw_json(response)
        except FileUploadException as ex:
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex:
            raise KaroException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def get_uploaded_document_number(self, request):
        data = FileUtil().get_uploaded_document_number(request.GET.get("transaction_id"),
                                                       request.GET.get("object_type"), )
        return self.send_response_raw_json(data)

    def get_all_files(self, request):
        data = FileUtil().get_all_files(request.GET.get("from_date"),
                                        request.GET.get("to_date"),
                                        request.GET.get("page_num"),
                                        request.GET.get("page_size"))
        return self.send_response_raw_json(data)

