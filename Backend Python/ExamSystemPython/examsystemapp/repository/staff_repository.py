"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.staff import StaffModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class StaffRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: StaffModel):
        self.sp_name = "sStaffAdd"
        list_params = [object.ownerid,object.role,object.name,object.staffnum,object.addr1,object.addr2,object.cityid,object.stateid,object.pin,object.phonenum,object.email,object.profilepic,object.loginid,object.password]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        staff_model: StaffModel = object
        staff_model.staffid= int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return staff_model

    def pre_update(self, object: StaffModel):
        self.sp_name = "sStaffUpdate"
        list_params = [object.staffid,object.ownerid,object.role,object.name,object.staffnum,object.addr1,object.addr2,object.cityid,object.stateid,object.pin,object.phonenum,object.email,object.profilepic,object.loginid,object.password]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        staff_model: StaffModel = object
        #staff_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return staff_model

    def pre_delete(self, object: StaffModel):
        self.sp_name = "sStaffDelete"
        list_params = [object.staffid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        staff_model: StaffModel = object
        staff_model.staffid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return staff_model

    def pre_get(self, params):
        self.sp_name = "sStaffGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            staff_model: StaffModel = StaffModel()
            for each_tuple in cursor_object.get_data():
                staff_model.staffid = each_tuple[0]
                staff_model.ownerid = each_tuple[1]
                staff_model.role = each_tuple[2]
                staff_model.name = each_tuple[3]
                staff_model.staffnum = each_tuple[4]
                staff_model.addr1 = each_tuple[5]
                staff_model.addr2 = each_tuple[6]
                staff_model.cityid = each_tuple[7]
                staff_model.stateid = each_tuple[8]
                staff_model.pin = each_tuple[9]
                staff_model.phonenum = each_tuple[10]
                staff_model.email = each_tuple[11]
                staff_model.profilepic = each_tuple[12]
                staff_model.loginid = each_tuple[13]
                staff_model.password = each_tuple[14]

            return staff_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sStaffGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                staff_model: StaffModel = StaffModel()
                staff_model.staffid = each_tuple[0]
                staff_model.ownerid = each_tuple[1]
                staff_model.role = each_tuple[2]
                staff_model.name = each_tuple[3]
                staff_model.staffnum = each_tuple[4]
                staff_model.addr1 = each_tuple[5]
                staff_model.addr2 = each_tuple[6]
                staff_model.cityid = each_tuple[7]
                staff_model.stateid = each_tuple[8]
                staff_model.pin = each_tuple[9]
                staff_model.phonenum = each_tuple[10]
                staff_model.email = each_tuple[11]
                staff_model.profilepic = each_tuple[12]
                staff_model.loginid = each_tuple[13]
                staff_model.password = each_tuple[14]

                list_data.append(staff_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sStaffObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sStaffObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sStaffGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
