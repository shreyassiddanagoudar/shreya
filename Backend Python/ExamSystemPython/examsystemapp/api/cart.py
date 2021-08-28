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
from examsystemapp.models.cart import CartModel
from examsystemapp.models.cart_item import CartItemModel
from examsystemapp.services.cart_service import CartService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Cart(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        cart_json = json.loads(request.POST.get("cart_json"))

        cart_object: CartModel = CartModel()
        cart_object.sessionid = cart_json.get("sessionid")
        cart_object.customerid = cart_json.get("customerid")

        cart_item = cart_json.get("cartitem")

        cart_item_model: CartItemModel = CartItemModel()
        cart_item_model.productid = cart_item.get("productid")
        cart_item_model.qty = cart_item.get("qty")
        cart_item_model.price = cart_item.get("price")

        cart_object.item = cart_item_model

        cart_service: CartService = CartService()
        cart_object = cart_service.add(cart_object)

        return self.send_response(cart_object)

    def update(self, request: HttpRequest):
        cart_json = json.loads(request.POST.get("cart_json"))

        cart_object: CartModel = CartModel()
        cart_object.cartid = cart_json.get("cartid")
        cart_object.sessionid = cart_json.get("sessionid")
        cart_object.customerid = cart_json.get("customerid")

        cart_service: CartService = CartService()
        cart_object = cart_service.update(cart_object)

        return self.send_response(cart_object)

    def delete(self, request: HttpRequest):
        cart_json = json.loads(request.POST.get("cart_json"))

        cart_object: CartModel = CartModel()
        cart_object.cartid = cart_json.get("cartid")

        cart_service: CartService = CartService()
        cart_object = cart_service.delete(cart_object)

        return self.send_response(cart_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        cart_service: CartService = CartService()
        data = cart_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        cart_service: CartService = CartService()
        data = cart_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = [
            {"sessionid": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')},
            {"customerid": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=None)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        cart_service: CartService = CartService()
        data = cart_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        cart_service: CartService = CartService()
        data = cart_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        cart_service: CartService = CartService()
        data = cart_service.get_list_object_paginated(params)
        return self.send_response(data)

    def delete_item(self, request: HttpRequest):
        cart_json = json.loads(request.POST.get("cart_json"))

        cartid = cart_json.get("cartid")
        productid = cart_json.get("productid")

        cart_service: CartService = CartService()
        cart_object = cart_service.delete_item(cartid, productid)

        return self.send_response(cart_object)

    def update_item(self, request: HttpRequest):
        cart_json = json.loads(request.POST.get("cart_json"))

        """
        {
            "cartitemid": 1,
            "qty": 1
        }
        """

        cartitemid = cart_json.get("cartitem_id")
        qty = cart_json.get("qty")

        cart_service: CartService = CartService()
        cart_object = cart_service.delete_item(cartitemid, qty)

        return self.send_response(cart_object)
