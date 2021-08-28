"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.student_ay import StudentAYModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class StudentAYRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: StudentAYModel):
        self.sp_name = "sStudentAYAdd"
        list_params = [object.studentid,object.ayid,object.semesterid,object.startdate,object.enddate]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        student_ay_model: StudentAYModel = object
        student_ay_model.studentayid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return student_ay_model

    def pre_update(self, object: StudentAYModel):
        self.sp_name = "sStudentAYUpdate"
        list_params = [object.studentayid,object.studentid,object.ayid,object.semesterid,object.startdate,object.enddate]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        student_ay_model: StudentAYModel = object
        student_ay_model.studentayid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return student_ay_model

    def pre_delete(self, object: StudentAYModel):
        self.sp_name = "sStudentAYDelete"
        list_params = [object.studentayid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        student_ay_model: StudentAYModel = object
        student_ay_model.studentayid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return student_ay_model

    def pre_get(self, params):
        self.sp_name = "sStudentAYGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            student_ay_model: StudentAYModel = StudentAYModel()
            for each_tuple in cursor_object.get_data():
                student_ay_model.studentayid = each_tuple[0]
                student_ay_model.studentid = each_tuple[1]
                student_ay_model.ayid = each_tuple[2]
                student_ay_model.semesterid = each_tuple[3]
                student_ay_model.startdate = each_tuple[4]
                student_ay_model.enddate = each_tuple[5]

            return student_ay_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sStudentAYGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                student_ay_model: StudentAYModel = StudentAYModel()
                student_ay_model.studentayid = each_tuple[0]
                student_ay_model.studentid = each_tuple[1]
                student_ay_model.ayid = each_tuple[2]
                student_ay_model.semesterid = each_tuple[3]
                student_ay_model.startdate = each_tuple[4]
                student_ay_model.enddate = each_tuple[5]

                list_data.append(student_ay_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sStudentAYObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sStudentAYObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sStudentAYGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
