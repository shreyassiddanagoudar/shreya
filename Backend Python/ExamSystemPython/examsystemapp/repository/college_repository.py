"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.college import CollegeModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CollegeRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CollegeModel):
        self.sp_name = "sCollegeAdd"
        list_params = [object.universityid,object.name,object.code,object.addr1,object.addr2,object.addr3,object.cityid,object.stateid,object.pincode,object.phone,object.email,object.logo,object.url]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        college_model: CollegeModel = object
        college_model.collegeid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return college_model

    def pre_update(self, object: CollegeModel):
        self.sp_name = "sCollegeUpdate"
        list_params = [object.collegeid,object.universityid,object.name,object.code,object.addr1,object.addr2,object.addr3,object.cityid,object.stateid,object.pincode,object.phone,object.email,object.logo,object.url]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        college_model: CollegeModel = object
        college_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return college_model

    def pre_delete(self, object: CollegeModel):
        self.sp_name = "sCollegeDelete"
        list_params = [object.collegeid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        college_model: CollegeModel = object
        college_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return college_model

    def pre_get(self, params):
        self.sp_name = "sCollegeGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            college_model: CollegeModel = CollegeModel()
            for each_tuple in cursor_object.get_data():
                college_model.collegeid = each_tuple[0]
                college_model.universityid = each_tuple[1]
                college_model.name = each_tuple[2]
                college_model.code = each_tuple[3]
                college_model.addr1 = each_tuple[4]
                college_model.addr2 = each_tuple[5]
                college_model.addr3 = each_tuple[6]
                college_model.cityid = each_tuple[7]
                college_model.stateid = each_tuple[8]
                college_model.pincode = each_tuple[9]
                college_model.phone = each_tuple[10]
                college_model.email = each_tuple[11]
                college_model.logo = each_tuple[12]
                college_model.url = each_tuple[13]

            return college_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCollegeGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                college_model: CollegeModel = CollegeModel()
                college_model.collegeid = each_tuple[0]
                college_model.universityid = each_tuple[1]
                college_model.name = each_tuple[2]
                college_model.code = each_tuple[3]
                college_model.addr1 = each_tuple[4]
                college_model.addr2 = each_tuple[5]
                college_model.addr3 = each_tuple[6]
                college_model.cityid = each_tuple[7]
                college_model.stateid = each_tuple[8]
                college_model.pincode = each_tuple[9]
                college_model.phone = each_tuple[10]
                college_model.email = each_tuple[11]
                college_model.logo = each_tuple[12]
                college_model.url = each_tuple[13]

                list_data.append(college_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCollegeObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCollegeObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCollegeGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None