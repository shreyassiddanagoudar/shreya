"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.college_branch import CollegeBranchModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CollegeBranchRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CollegeBranchModel):
        self.sp_name = "sCollegeBranchAdd"
        list_params = [object.collegebranchid,object.branchid,object.collegeid,object.phonenum,object.email,object.url]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        college_branch_model: CollegeBranchModel = object
        college_branch_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return college_branch_model

    def pre_update(self, object: CollegeBranchModel):
        self.sp_name = "sCollegeBranchUpdate"
        list_params = [object.collegebranchid,object.branchid,object.collegeid,object.phonenum,object.email,object.url]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        college_branch_model: CollegeBranchModel = object
        college_branch_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return college_branch_model

    def pre_delete(self, object: CollegeBranchModel):
        self.sp_name = "sCollegeBranchDelete"
        list_params = [object.collegebranchid,object.branchid,object.collegeid,object.phonenum,object.email,object.url]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        college_branch_model: CollegeBranchModel = object
        college_branch_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return college_branch_model

    def pre_get(self, params):
        self.sp_name = "sCollegeBranchGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            college_branch_model: CollegeBranchModel = CollegeBranchModel()
            for each_tuple in cursor_object.get_data():
                college_branch_model.collegebranchid = each_tuple[0]
                college_branch_model.branchid = each_tuple[1]
                college_branch_model.collegeid = each_tuple[2]
                college_branch_model.phonenum = each_tuple[3]
                college_branch_model.email = each_tuple[4]
                college_branch_model.url = each_tuple[5]

            return college_branch_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCollegeBranchGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                college_branch_model: CollegeBranchModel = CollegeBranchModel()
                college_branch_model.collegebranchid = each_tuple[0]
                college_branch_model.branchid = each_tuple[1]
                college_branch_model.collegeid = each_tuple[2]
                college_branch_model.phonenum = each_tuple[3]
                college_branch_model.email = each_tuple[4]
                college_branch_model.url = each_tuple[5]

                list_data.append(college_branch_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCollegeBranchObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCollegeBranchObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCollegeBranchObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
