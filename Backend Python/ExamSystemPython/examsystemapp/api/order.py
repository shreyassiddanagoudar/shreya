"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from django.http import HttpRequest
from examsystemapp.api.base_controller import BaseController
from examsystemapp.models.order import OrderModel
from examsystemapp.models.order_item import OrderItemModel
from examsystemapp.services.order_service import OrderService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Order(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        order_json = json.loads(request.POST.get("order_json"))

        order_object: OrderModel = OrderModel()
       
        order_object.customerid = order_json.get("customerid")
    
        order_object.addressid = order_json.get("addressid")
        order_object.paymenttype = order_json.get("paymenttype")
        order_object.paymentstatus = order_json.get("paymentstatus")
        order_object.totalprice = order_json.get("totalprice")
        
        order_object.items = []
        order_item = order_json.get("orderitem")
        for items in order_item:
            order_item_model: OrderItemModel = OrderItemModel()
            order_item_model.productid = items.get("productid")
            order_item_model.qty = items.get("qty")
            order_item_model.price = items.get("price")
            order_object.items.append(order_item_model)
            
        order_service: OrderService = OrderService()
        order_object = order_service.add(order_object)

        return self.send_response(order_object)

    def update(self, request: HttpRequest):
        order_json = json.loads(request.POST.get("order_json"))

        order_object: OrderModel = OrderModel()
        order_object.orderid = order_json.get("orderid")
        order_object.customerid = order_json.get("customerid")
        order_object.orderdate = order_json.get("orderdate")
        order_object.status = order_json.get("status")
        order_object.addressid = order_json.get("addressid")
        order_object.paymenttype = order_json.get("paymenttype")
        order_object.paymentstatus = order_json.get("paymentstatus")
        order_object.totalprice = order_json.get("totalprice")

        order_service: OrderService = OrderService()
        order_object = order_service.update(order_object)

        return self.send_response(order_object)

    def delete(self, request: HttpRequest):
        order_json = json.loads(request.POST.get("order_json"))

        order_object: OrderModel = OrderModel()
        order_object.orderid = order_json.get("orderid")
        order_object.customerid = order_json.get("customerid")
        order_object.orderdate = order_json.get("orderdate")
        order_object.status = order_json.get("status")
        order_object.addressid = order_json.get("addressid")
        order_object.paymenttype = order_json.get("paymenttype")
        order_object.paymentstatus = order_json.get("paymentstatus")
        order_object.totalprice = order_json.get("totalprice")

        

        order_service: OrderService = OrderService()
        order_object = order_service.delete(order_object)

        return self.send_response(order_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        order_service: OrderService = OrderService()
        data = order_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        order_service: OrderService = OrderService()
        data = order_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        order_service: OrderService = OrderService()
        data = order_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        order_service: OrderService = OrderService()
        data = order_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"customerid": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default='')},
            {"page_num": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)},
            {"page_size": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=15)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        order_service: OrderService = OrderService()
        data = order_service.get_list_object_paginated(params)
        return self.send_response(data)
