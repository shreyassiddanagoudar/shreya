"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.cart_item import CartItemModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CartItemRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CartItemModel):
        self.sp_name = "sCartItemAdd"
        list_params = [object.cartid, object.productid, object.qty, object.price]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        cart_item_model: CartItemModel = object
        cart_item_model.cartitemid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return cart_item_model

    def pre_update(self, object: CartItemModel):
        self.sp_name = "sCartItemUpdate"
        list_params = [object.cartitemid, object.cartid, object.date, object.productid, object.qty, object.price]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        cart_item_model: CartItemModel = object
        cart_item_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return cart_item_model

    def pre_delete(self, object: CartItemModel):
        self.sp_name = "sCartItemDelete"
        list_params = [object.cartitemid, object.cartid, object.date, object.productid, object.qty, object.price]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        cart_item_model: CartItemModel = object
        cart_item_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return cart_item_model

    def pre_get(self, params):
        self.sp_name = "sCartItemGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            cart_item_model: CartItemModel = CartItemModel()
            for each_tuple in cursor_object.get_data():
                cart_item_model.cartitemid = each_tuple[0]
                cart_item_model.cartid = each_tuple[1]
                cart_item_model.date = each_tuple[2]
                cart_item_model.productid = each_tuple[3]
                cart_item_model.qty = each_tuple[4]
                cart_item_model.price = each_tuple[5]

            return cart_item_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCartItemGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                cart_item_model: CartItemModel = CartItemModel()
                cart_item_model.cartitemid = each_tuple[0]
                cart_item_model.cartid = each_tuple[1]
                cart_item_model.date = str(each_tuple[2])
                cart_item_model.productid = each_tuple[3]
                cart_item_model.qty = each_tuple[4]
                cart_item_model.price = each_tuple[5]

                cart_item_model.productname = each_tuple[6]
                cart_item_model.description = each_tuple[7]
                cart_item_model.imageurl = each_tuple[8]
                cart_item_model.brand = each_tuple[9]

                list_data.append(cart_item_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCartItemObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCartItemObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCartItemObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
