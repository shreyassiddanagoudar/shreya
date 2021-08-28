"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.bs_subject_hdr import BSSubjectHdrModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class BSSubjectHdrRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: BSSubjectHdrModel):
        self.sp_name = "sBSSubjectHdrAdd"
        list_params = [object.branchsubjectid,object.branchid,object.semesterid]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        bs_subject_hdr_model: BSSubjectHdrModel = object
        bs_subject_hdr_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return bs_subject_hdr_model

    def pre_update(self, object: BSSubjectHdrModel):
        self.sp_name = "sBSSubjectHdrUpdate"
        list_params = [object.branchsubjectid,object.branchid,object.semesterid]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        bs_subject_hdr_model: BSSubjectHdrModel = object
        bs_subject_hdr_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return bs_subject_hdr_model

    def pre_delete(self, object: BSSubjectHdrModel):
        self.sp_name = "sBSSubjectHdrDelete"
        list_params = [object.branchsubjectid,object.branchid,object.semesterid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        bs_subject_hdr_model: BSSubjectHdrModel = object
        bs_subject_hdr_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return bs_subject_hdr_model

    def pre_get(self, params):
        self.sp_name = "sBSSubjectHdrGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            bs_subject_hdr_model: BSSubjectHdrModel = BSSubjectHdrModel()
            for each_tuple in cursor_object.get_data():
                bs_subject_hdr_model.branchsubjectid = each_tuple[0]
                bs_subject_hdr_model.branchid = each_tuple[1]
                bs_subject_hdr_model.semesterid = each_tuple[2]

            return bs_subject_hdr_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sBSSubjectHdrGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                bs_subject_hdr_model: BSSubjectHdrModel = BSSubjectHdrModel()
                bs_subject_hdr_model.branchsubjectid = each_tuple[0]
                bs_subject_hdr_model.branchid = each_tuple[1]
                bs_subject_hdr_model.semesterid = each_tuple[2]

                list_data.append(bs_subject_hdr_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sBSSubjectHdrObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sBSSubjectHdrObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sBSSubjectHdrObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
