"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.student import StudentModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class StudentRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: StudentModel):
        self.sp_name = "sStudentAdd"
        list_params = [object.collegeid,object.branchid,object.currentsemester,object.name,object.rollno,object.add1,object.add2,object.add3,object.cityid,object.stateid,object.pin,object.phonenum,object.email,object.profilepic,object.loginid,object.passwd]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        student_model: StudentModel = object
        student_model.studentid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return student_model

    def pre_update(self, object: StudentModel):
        self.sp_name = "sStudentUpdate"
        list_params = [object.studentid,object.collegeid,object.branchid,object.currentsemester,object.name,object.rollno,object.add1,object.add2,object.add3,object.cityid,object.stateid,object.pin,object.phonenum,object.email,object.profilepic,object.loginid,object.passwd]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        student_model: StudentModel = object
        student_model.studentid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return student_model

    def pre_delete(self, object: StudentModel):
        self.sp_name = "sStudentDelete"
        list_params = [object.studentid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        student_model: StudentModel = object
        student_model.studentid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return student_model

    def pre_get(self, params):
        self.sp_name = "sStudentGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            student_model: StudentModel = StudentModel()
            for each_tuple in cursor_object.get_data():
                student_model.studentid = each_tuple[0]
                student_model.collegeid = each_tuple[1]
                student_model.branchid = each_tuple[2]
                student_model.currentsemester = each_tuple[3]
                student_model.name = each_tuple[4]
                student_model.rollno = each_tuple[5]
                student_model.add1 = each_tuple[6]
                student_model.add2 = each_tuple[7]
                student_model.add3 = each_tuple[8]
                student_model.cityid = each_tuple[9]
                student_model.stateid = each_tuple[10]
                student_model.pin = each_tuple[11]
                student_model.phonenum = each_tuple[12]
                student_model.email = each_tuple[13]
                student_model.profilepic = each_tuple[14]
                student_model.loginid = each_tuple[15]
                student_model.passwd = each_tuple[16]

            return student_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sStudentGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                student_model: StudentModel = StudentModel()
                student_model.studentid = each_tuple[0]
                student_model.collegeid = each_tuple[1]
                student_model.branchid = each_tuple[2]
                student_model.currentsemester = each_tuple[3]
                student_model.name = each_tuple[4]
                student_model.rollno = each_tuple[5]
                student_model.add1 = each_tuple[6]
                student_model.add2 = each_tuple[7]
                student_model.add3 = each_tuple[8]
                student_model.cityid = each_tuple[9]
                student_model.stateid = each_tuple[10]
                student_model.pin = each_tuple[11]
                student_model.phonenum = each_tuple[12]
                student_model.email = each_tuple[13]
                student_model.profilepic = each_tuple[14]
                student_model.loginid = each_tuple[15]
                student_model.passwd = each_tuple[16]

                list_data.append(student_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sStudentObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sStudentObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sStudentGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
