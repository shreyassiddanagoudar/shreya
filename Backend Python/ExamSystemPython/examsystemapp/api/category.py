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
from examsystemapp.models.category import CategoryModel
from examsystemapp.services.category_service import CategoryService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Category(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        category_json = json.loads(request.POST.get("category_json"))

        category_object: CategoryModel = CategoryModel()
        category_object.categoryid = category_json.get("categoryid")
        category_object.name = category_json.get("name")
        category_object.description = category_json.get("description")
        category_object.imageurl = category_json.get("imageurl")

        category_service: CategoryService = CategoryService()
        category_object = category_service.add(category_object)

        return self.send_response(category_object)

    def update(self, request: HttpRequest):
        category_json = json.loads(request.POST.get("category_json"))

        category_object: CategoryModel = CategoryModel()
        category_object.categoryid = category_json.get("categoryid")
        category_object.name = category_json.get("name")
        category_object.description = category_json.get("description")
        category_object.imageurl = category_json.get("imageurl")

        category_service: CategoryService = CategoryService()
        category_object = category_service.update(category_object)

        return self.send_response(category_object)

    def delete(self, request: HttpRequest):
        category_json = json.loads(request.POST.get("category_json"))

        category_object: CategoryModel = CategoryModel()
        category_object.categoryid = category_json.get("categoryid")
        category_object.name = category_json.get("name")
        category_object.description = category_json.get("description")
        category_object.imageurl = category_json.get("imageurl")

        category_service: CategoryService = CategoryService()
        category_object = category_service.delete(category_object)

        return self.send_response(category_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        category_service: CategoryService = CategoryService()
        data = category_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        category_service: CategoryService = CategoryService()
        data = category_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        category_service: CategoryService = CategoryService()
        data = category_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        category_service: CategoryService = CategoryService()
        data = category_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        category_service: CategoryService = CategoryService()
        data = category_service.get_list_object_paginated(params)
        return self.send_response(data)

    def get_menu(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        category_service: CategoryService = CategoryService()
        data = category_service.get_menu()
        return self.send_response(data)
