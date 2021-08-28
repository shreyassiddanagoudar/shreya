"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.order import OrderModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.repository.order_item_repository import OrderItemRepo
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class OrderRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: OrderModel):
        self.sp_name = "sOrderAdd"
        list_params = [object.customerid,object.addressid,object.paymenttype,object.paymentstatus,object.totalprice]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        order_model: OrderModel = object
        order_model.orderid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))
        
        for items in order_model.items:
            order_item_repo: OrderItemRepo = OrderItemRepo()
            items.orderid = order_model.orderid
            order_item_repo.add_data(items)

        # Delete the cart
        # Create CartModel()
        # Add customer_id into the model
        # Call CartRepo().delete_data(cart_model)
        
        cart_model: CartModel = CartModel()
        cart_model.customerid = order_model.customerid
        cart_repo: CartRepo = CartRepo()
        cart_repo.delete_data(cart_model)


        return order_model

    def pre_update(self, object: OrderModel):
        self.sp_name = "sOrderUpdate"
        list_params = [object.orderid,object.customerid,object.orderdate,object.status,object.addressid,object.paymenttype,object.paymentstatus,object.totalprice]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        order_model: OrderModel = object
        order_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return order_model

    def pre_delete(self, object: OrderModel):
        self.sp_name = "sOrderDelete"
        list_params = [object.orderid,object.customerid,object.orderdate,object.status,object.addressid,object.paymenttype,object.paymentstatus,object.totalprice]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        order_model: OrderModel = object
        order_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return order_model

    def pre_get(self, params):
        self.sp_name = "sOrderGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            order_model: OrderModel = OrderModel()
            for each_tuple in cursor_object.get_data():
                order_model.orderid = each_tuple[0]
                order_model.customerid = each_tuple[1]
                order_model.orderdate = each_tuple[2]
                order_model.status = each_tuple[3]
                order_model.addressid = each_tuple[4]
                order_model.paymenttype = each_tuple[5]
                order_model.paymentstatus = each_tuple[6]
                order_model.totalprice = each_tuple[7]

            return order_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sOrderGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                order_model: OrderModel = OrderModel()
                order_model.orderid = each_tuple[0]
                order_model.customerid = each_tuple[1]
                order_model.orderdate = str(each_tuple[2])
                order_model.status = each_tuple[3]
                order_model.addressid = each_tuple[4]
                order_model.paymenttype = each_tuple[5]
                order_model.paymentstatus = each_tuple[6]
                order_model.totalprice = each_tuple[7]
                
                params: ParamsObject = ParamsObject()
                params.set_params_list([order_model.orderid])
                order_model.items = OrderItemRepo().get_data_list(params)

                list_data.append(order_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sOrderObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sOrderObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sOrderGetList"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
