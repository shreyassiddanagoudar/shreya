"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.product import ProductModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class ProductRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: ProductModel):
        self.sp_name = "sProductAdd"
        list_params = [object.productid, object.name, object.description, object.brandid, object.imageurl, object.price,
                       object.subcategoryid]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        product_model: ProductModel = object
        product_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return product_model

    def pre_update(self, object: ProductModel):
        self.sp_name = "sProductUpdate"
        list_params = [object.productid, object.name, object.description, object.brandid, object.imageurl, object.price,
                       object.subcategoryid]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        product_model: ProductModel = object
        product_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return product_model

    def pre_delete(self, object: ProductModel):
        self.sp_name = "sProductDelete"
        list_params = [object.productid, object.name, object.description, object.brandid, object.imageurl, object.price,
                       object.subcategoryid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        product_model: ProductModel = object
        product_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return product_model

    def pre_get(self, params):
        self.sp_name = "sProductGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            product_model: ProductModel = ProductModel()
            for each_tuple in cursor_object.get_data():
                product_model.productid = each_tuple[0]
                product_model.name = each_tuple[1]
                product_model.description = each_tuple[2]
                product_model.brandid = each_tuple[3]
                product_model.imageurl = each_tuple[4]
                product_model.price = each_tuple[5]
                product_model.subcategoryid = each_tuple[6]

            return product_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sProductGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                product_model: ProductModel = ProductModel()
                product_model.productid = each_tuple[0]
                product_model.name = each_tuple[1]
                product_model.description = each_tuple[2]
                product_model.brandid = each_tuple[3]
                product_model.imageurl = each_tuple[4]
                product_model.price = each_tuple[5]
                product_model.subcategoryid = each_tuple[6]

                list_data.append(product_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sProductObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sProductObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sProductObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None

    def get_products_by_subcategory(self, params: ParamsObject):
        return self.get_direct_multiple("sGetProductBySubCategory", params.get_params_list())

    
    def get_products_by_search(self, params: ParamsObject):
        return self.get_direct_multiple("sGetProductBySearch", params.get_params_list())
