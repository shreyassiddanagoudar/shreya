"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.university_ay import UniversityAYModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class UniversityAYRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: UniversityAYModel):
        self.sp_name = "sUniversityAYAdd"
        list_params = [object.ayid,object.universityid,object.startdate,object.enddate]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        university_ay_model: UniversityAYModel = object
        university_ay_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return university_ay_model

    def pre_update(self, object: UniversityAYModel):
        self.sp_name = "sUniversityAYUpdate"
        list_params = [object.ayid,object.universityid,object.startdate,object.enddate]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        university_ay_model: UniversityAYModel = object
        university_ay_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return university_ay_model

    def pre_delete(self, object: UniversityAYModel):
        self.sp_name = "sUniversityAYDelete"
        list_params = [object.ayid,object.universityid,object.startdate,object.enddate]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        university_ay_model: UniversityAYModel = object
        university_ay_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return university_ay_model

    def pre_get(self, params):
        self.sp_name = "sUniversityAYGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            university_ay_model: UniversityAYModel = UniversityAYModel()
            for each_tuple in cursor_object.get_data():
                university_ay_model.ayid = each_tuple[0]
                university_ay_model.universityid = each_tuple[1]
                university_ay_model.startdate = each_tuple[2]
                university_ay_model.enddate = each_tuple[3]

            return university_ay_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sUniversityAYGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                university_ay_model: UniversityAYModel = UniversityAYModel()
                university_ay_model.ayid = each_tuple[0]
                university_ay_model.universityid = each_tuple[1]
                university_ay_model.startdate = each_tuple[2]
                university_ay_model.enddate = each_tuple[3]

                list_data.append(university_ay_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sUniversityAYObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sUniversityAYObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sUniversityAYObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
