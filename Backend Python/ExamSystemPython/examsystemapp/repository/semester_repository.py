"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.semester import SemesterModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class SemesterRepo(BaseRepository):

    def _init_(self, ext_params={}):
        BaseRepository._init_(self, ext_params)

    def pre_add(self, object: SemesterModel):
        self.sp_name = "ssemesterAdd"
        list_params = [object.name,object.code]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        semester_model: SemesterModel = object
        semester_model.semesterid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return semester_model

    def pre_update(self, object: SemesterModel):
        self.sp_name = "ssemesterUpdate"
        list_params = [object.semesterid,object.name,object.code]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        semester_model: SemesterModel = object
        #semester_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return semester_model

    def pre_delete(self, object: SemesterModel):
        self.sp_name = "ssemesterDelete"
        list_params = [object.semesterid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        semester_model: SemesterModel = object
        semester_model.semesterid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return semester_model

    def pre_get(self, params):
        self.sp_name = "ssemesterGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            semester_model: SemesterModel = SemesterModel()
            for each_tuple in cursor_object.get_data():
                semester_model.semesterid = each_tuple[0]
                semester_model.name = each_tuple[1]
                semester_model.code = each_tuple[2]

            return semester_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "ssemesterGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                semester_model: SemesterModel = SemesterModel()
                semester_model.semesterid = each_tuple[0]
                semester_model.name = each_tuple[1]
                semester_model.code = each_tuple[2]

                list_data.append(semester_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "ssemesterObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "ssemesterObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "ssemesterGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None