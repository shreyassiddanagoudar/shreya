"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.category import CategoryModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CategoryRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CategoryModel):
        self.sp_name = "sCategoryAdd"
        list_params = [object.categoryid,object.name,object.description,object.imageurl]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        category_model: CategoryModel = object
        category_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return category_model

    def pre_update(self, object: CategoryModel):
        self.sp_name = "sCategoryUpdate"
        list_params = [object.categoryid,object.name,object.description,object.imageurl]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        category_model: CategoryModel = object
        category_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return category_model

    def pre_delete(self, object: CategoryModel):
        self.sp_name = "sCategoryDelete"
        list_params = [object.categoryid,object.name,object.description,object.imageurl]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        category_model: CategoryModel = object
        category_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return category_model

    def pre_get(self, params):
        self.sp_name = "sCategoryGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            category_model: CategoryModel = CategoryModel()
            for each_tuple in cursor_object.get_data():
                category_model.categoryid = each_tuple[0]
                category_model.name = each_tuple[1]
                category_model.description = each_tuple[2]
                category_model.imageurl = each_tuple[3]

            return category_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCategoryGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                category_model: CategoryModel = CategoryModel()
                category_model.categoryid = each_tuple[0]
                category_model.name = each_tuple[1]
                category_model.description = each_tuple[2]
                category_model.imageurl = each_tuple[3]

                list_data.append(category_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCategoryObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCategoryObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCategoryObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None

    def get_menu(self):
        """ I need to call Category Get List """
        category_list = self.get_direct("sGetCategoryList", [None]) # This returns list / array of categories

        for category in category_list:
            """ category is dictionary """
            print(category)
            print(category.get("CategoryID"))
            sub_categories = self.get_direct("sGetSubCategoryByParent", [category.get("CategoryID")])
            category["SubCategories"] = sub_categories

        return category_list


