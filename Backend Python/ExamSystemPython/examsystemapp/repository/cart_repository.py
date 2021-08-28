"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.cart import CartModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.repository.cart_item_repository import CartItemRepo
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CartRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CartModel):
        self.sp_name = "sCartAdd"
        list_params = [object.sessionid, object.customerid]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        cart_model: CartModel = object
        cart_model.cartid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        """
        Need to add the Items into the cart
        """
        cart_item_repo: CartItemRepo = CartItemRepo()
        cart_model.item.cartid = cart_model.cartid
        cart_item_repo.add_data(cart_model.item)

        return cart_model

    def pre_update(self, object: CartModel):
        self.sp_name = "sCartUpdate"
        list_params = [object.cartid, object.sessionid, object.customerid]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        cart_model: CartModel = object
        cart_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return cart_model

    def pre_delete(self, object: CartModel):
        self.sp_name = "sCartDelete"
        list_params = [object.customerid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        cart_model: CartModel = object

        return cart_model

    def pre_get(self, params):
        self.sp_name = "sCartGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            cart_model: CartModel = CartModel()
            for each_tuple in cursor_object.get_data():
                cart_model.cartid = each_tuple[0]
                cart_model.sessionid = each_tuple[1]
                cart_model.customerid = each_tuple[2]

                """
                Get the Cart Items for this cart
                """
                params: ParamsObject = ParamsObject()
                params.set_params_list([cart_model.cartid])
                cart_model.items = CartItemRepo().get_data_list(params)

            return cart_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCartGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                cart_model: CartModel = CartModel()
                cart_model.cartid = each_tuple[0]
                cart_model.sessionid = each_tuple[1]
                cart_model.customerid = each_tuple[2]

                list_data.append(cart_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCartGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCartObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCartObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
