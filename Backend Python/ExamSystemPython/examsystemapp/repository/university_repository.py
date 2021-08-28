"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.university             import UniversityModel
from examsystemapp.repository.base_repository    import BaseRepository
from examsystemapp.utils.constants.constants     import AppConstants
from examsystemapp.utils.helpers.general_helper  import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper  import ParamsObject


class UniversityRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: UniversityModel):
        self.sp_name = "sUniversityAdd"
        list_params = [object.name,object.code,object.addr1,object.addr2,object.addr3,object.cityid,object.stateid,object.pincode,object.phone,object.email,object.logo,object.url]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        university_model: UniversityModel = object
        university_model.universityid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return university_model

    def pre_update(self, object: UniversityModel):
        self.sp_name = "sUniversityUpdate"
        list_params = [object.universityid,object.name,object.code,object.addr1,object.addr2,object.addr3,object.cityid,object.stateid,object.pincode,object.phone,object.email,object.logo,object.url]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        university_model: UniversityModel = object
        university_model.universityid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return university_model

    def pre_delete(self, object: UniversityModel):
        self.sp_name = "sUniversityDelete"
        list_params = [object.universityid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        university_model: UniversityModel = object
        university_model.universityid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return university_model

    def pre_get(self, params):
        self.sp_name = "sUniversityGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            university_model: UniversityModel = UniversityModel()
            for each_tuple in cursor_object.get_data():
                university_model.universityid = each_tuple[0]
                university_model.name         = each_tuple[1]
                university_model.code         = each_tuple[2]
                university_model.addr1        = each_tuple[3]
                university_model.addr2        = each_tuple[4]
                university_model.addr3        = each_tuple[5]
                university_model.cityid       = each_tuple[6]
                university_model.stateid      = each_tuple[7]
                university_model.pincode      = each_tuple[8]
                university_model.url          = each_tuple[12]
                university_model.phone        = each_tuple[9]
                university_model.email        = each_tuple[10]
                university_model.logo         = each_tuple[11]

            return university_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sUniversityGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                university_model: UniversityModel = UniversityModel()
                university_model.universityid = each_tuple[0]
                university_model.name         = each_tuple[1]
                university_model.code         = each_tuple[2]
                university_model.addr1        = each_tuple[3]
                university_model.addr2        = each_tuple[4]
                university_model.addr3        = each_tuple[5]
                university_model.cityid       = each_tuple[6]
                university_model.stateid      = each_tuple[7]
                university_model.pincode      = each_tuple[8]
                university_model.phone        = each_tuple[9]
                university_model.email        = each_tuple[10]
                university_model.logo         = each_tuple[11]
                university_model.url          = each_tuple[12]

                list_data.append(university_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sUniversityObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sUniversityObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sUniversityGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
