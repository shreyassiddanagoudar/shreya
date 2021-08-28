"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.sub_category import SubCategoryModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class SubCategoryRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: SubCategoryModel):
        self.sp_name = "sSubCategoryAdd"
        list_params = [object.subcategoryid,object.name,object.parentcategoryid,object.parentsubcategoryid,object.description,object.imageurl]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        sub_category_model: SubCategoryModel = object
        sub_category_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return sub_category_model

    def pre_update(self, object: SubCategoryModel):
        self.sp_name = "sSubCategoryUpdate"
        list_params = [object.subcategoryid,object.name,object.parentcategoryid,object.parentsubcategoryid,object.description,object.imageurl]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        sub_category_model: SubCategoryModel = object
        sub_category_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return sub_category_model

    def pre_delete(self, object: SubCategoryModel):
        self.sp_name = "sSubCategoryDelete"
        list_params = [object.subcategoryid,object.name,object.parentcategoryid,object.parentsubcategoryid,object.description,object.imageurl]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        sub_category_model: SubCategoryModel = object
        sub_category_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return sub_category_model

    def pre_get(self, params):
        self.sp_name = "sSubCategoryGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            sub_category_model: SubCategoryModel = SubCategoryModel()
            for each_tuple in cursor_object.get_data():
                sub_category_model.subcategoryid = each_tuple[0]
                sub_category_model.name = each_tuple[1]
                sub_category_model.parentcategoryid = each_tuple[2]
                sub_category_model.parentsubcategoryid = each_tuple[3]
                sub_category_model.description = each_tuple[4]
                sub_category_model.imageurl = each_tuple[5]

            return sub_category_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sSubCategoryGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                sub_category_model: SubCategoryModel = SubCategoryModel()
                sub_category_model.subcategoryid = each_tuple[0]
                sub_category_model.name = each_tuple[1]
                sub_category_model.parentcategoryid = each_tuple[2]
                sub_category_model.parentsubcategoryid = each_tuple[3]
                sub_category_model.description = each_tuple[4]
                sub_category_model.imageurl = each_tuple[5]

                list_data.append(sub_category_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sSubCategoryObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sSubCategoryObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sSubCategoryObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
