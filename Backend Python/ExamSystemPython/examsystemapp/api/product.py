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
from examsystemapp.models.product import ProductModel
from examsystemapp.services.product_service import ProductService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Product(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        product_json = json.loads(request.POST.get("product_json"))

        product_object: ProductModel = ProductModel()
        product_object.productid = product_json.get("productid")
        product_object.name = product_json.get("name")
        product_object.description = product_json.get("description")
        product_object.brandid = product_json.get("brandid")
        product_object.imageurl = product_json.get("imageurl")
        product_object.price = product_json.get("price")
        product_object.subcategoryid = product_json.get("subcategoryid")

        product_service: ProductService = ProductService()
        product_object = product_service.add(product_object)

        return self.send_response(product_object)

    def update(self, request: HttpRequest):
        product_json = json.loads(request.POST.get("product_json"))

        product_object: ProductModel = ProductModel()
        product_object.productid = product_json.get("productid")
        product_object.name = product_json.get("name")
        product_object.description = product_json.get("description")
        product_object.brandid = product_json.get("brandid")
        product_object.imageurl = product_json.get("imageurl")
        product_object.price = product_json.get("price")
        product_object.subcategoryid = product_json.get("subcategoryid")

        product_service: ProductService = ProductService()
        product_object = product_service.update(product_object)

        return self.send_response(product_object)

    def delete(self, request: HttpRequest):
        product_json = json.loads(request.POST.get("product_json"))

        product_object: ProductModel = ProductModel()
        product_object.productid = product_json.get("productid")
        product_object.name = product_json.get("name")
        product_object.description = product_json.get("description")
        product_object.brandid = product_json.get("brandid")
        product_object.imageurl = product_json.get("imageurl")
        product_object.price = product_json.get("price")
        product_object.subcategoryid = product_json.get("subcategoryid")

        product_service: ProductService = ProductService()
        product_object = product_service.delete(product_object)

        return self.send_response(product_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get_list_object_paginated(params)
        return self.send_response(data)

    def get_products_by_subcategory(self, request: HttpRequest):
        params = [
            {"sub_cat_id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default='')},
            {"page_num": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)},
            {"page_size": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=15)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get_products_by_subcategory(params)
        return self.send_response(data)

    def get_products_by_search(self, request: HttpRequest):
        params = [
            {"search": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')},
            {"page_num": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)},
            {"page_size": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=15)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        product_service: ProductService = ProductService()
        data = product_service.get_products_by_search(params)
        return self.send_response(data)
