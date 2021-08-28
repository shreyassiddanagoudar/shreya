"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.order_item import OrderItemModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class OrderItemRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: OrderItemModel):
        self.sp_name = "sOrderItemAdd"
        list_params = [object.orderid,object.productid,object.qty,object.price]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        order_item_model: OrderItemModel = object
        order_item_model.orderitemid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return order_item_model

    def pre_update(self, object: OrderItemModel):
        self.sp_name = "sOrderItemUpdate"
        list_params = [object.orderitemid,object.orderid,object.productid,object.qty,object.price,object.status]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        order_item_model: OrderItemModel = object
        order_item_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return order_item_model

    def pre_delete(self, object: OrderItemModel):
        self.sp_name = "sOrderItemDelete"
        list_params = [object.orderitemid,object.orderid,object.productid,object.qty,object.price,object.status]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        order_item_model: OrderItemModel = object
        order_item_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return order_item_model

    def pre_get(self, params):
        self.sp_name = "sOrderItemGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            order_item_model: OrderItemModel = OrderItemModel()
            for each_tuple in cursor_object.get_data():
                order_item_model.orderitemid = each_tuple[0]
                order_item_model.orderid = each_tuple[1]
                order_item_model.productid = each_tuple[2]
                order_item_model.qty = each_tuple[3]
                order_item_model.price = each_tuple[4]
                order_item_model.status = each_tuple[5]

            return order_item_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sOrderItemGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                order_item_model: OrderItemModel = OrderItemModel()
                order_item_model.orderitemid = each_tuple[0]
                order_item_model.orderid = each_tuple[1]
                order_item_model.productid = each_tuple[2]
                order_item_model.qty = each_tuple[3]
                order_item_model.price = each_tuple[4]
                order_item_model.status = each_tuple[5]
                order_item_model.productname = each_tuple[6]
                order_item_model.description = each_tuple[7]
                order_item_model.imageurl = each_tuple[8]
                order_item_model.brandid = each_tuple[9]
                order_item_model.brandname = each_tuple[10]


                list_data.append(order_item_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sOrderItemObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sOrderItemObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sOrderItemObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
