"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.branch import BranchModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class BranchRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: BranchModel):
        self.sp_name = "sBranchAdd"
        list_params = [object.name, object.code]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        branch_model: BranchModel = object
        branch_model.branchid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return branch_model

    def pre_update(self, object: BranchModel):
        self.sp_name = "sBranchUpdate"
        list_params = [object.branchid, object.name, object.code]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        branch_model: BranchModel = object
        # branch_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return branch_model

    def pre_delete(self, object: BranchModel):
        self.sp_name = "sBranchDelete"
        list_params = [object.branchid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        branch_model: BranchModel = object
        branch_model.branchid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return branch_model

    def pre_get(self, params):
        self.sp_name = "sBranchGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            branch_model: BranchModel = BranchModel()
            for each_tuple in cursor_object.get_data():
                branch_model.branchid = each_tuple[0]
                branch_model.name = each_tuple[1]
                branch_model.code = each_tuple[2]

            return branch_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sBranchGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                branch_model: BranchModel = BranchModel()
                branch_model.branchid = each_tuple[0]
                branch_model.name = each_tuple[1]
                branch_model.code = each_tuple[2]

                list_data.append(branch_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sBranchObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sBranchObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sBranchGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
