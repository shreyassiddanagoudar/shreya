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
from examsystemapp.models.sub_category import SubCategoryModel
from examsystemapp.services.sub_category_service import SubCategoryService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class SubCategory(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        sub_category_json = json.loads(request.POST.get("sub_category_json"))

        sub_category_object: SubCategoryModel = SubCategoryModel()
        sub_category_object.subcategoryid = sub_category_json.get("subcategoryid")
        sub_category_object.name = sub_category_json.get("name")
        sub_category_object.parentcategoryid = sub_category_json.get("parentcategoryid")
        sub_category_object.parentsubcategoryid = sub_category_json.get("parentsubcategoryid")
        sub_category_object.description = sub_category_json.get("description")
        sub_category_object.imageurl = sub_category_json.get("imageurl")

        sub_category_service: SubCategoryService = SubCategoryService()
        sub_category_object = sub_category_service.add(sub_category_object)

        return self.send_response(sub_category_object)

    def update(self, request: HttpRequest):
        sub_category_json = json.loads(request.POST.get("sub_category_json"))

        sub_category_object: SubCategoryModel = SubCategoryModel()
        sub_category_object.subcategoryid = sub_category_json.get("subcategoryid")
        sub_category_object.name = sub_category_json.get("name")
        sub_category_object.parentcategoryid = sub_category_json.get("parentcategoryid")
        sub_category_object.parentsubcategoryid = sub_category_json.get("parentsubcategoryid")
        sub_category_object.description = sub_category_json.get("description")
        sub_category_object.imageurl = sub_category_json.get("imageurl")

        sub_category_service: SubCategoryService = SubCategoryService()
        sub_category_object = sub_category_service.update(sub_category_object)

        return self.send_response(sub_category_object)

    def delete(self, request: HttpRequest):
        sub_category_json = json.loads(request.POST.get("sub_category_json"))

        sub_category_object: SubCategoryModel = SubCategoryModel()
        sub_category_object.subcategoryid = sub_category_json.get("subcategoryid")
        sub_category_object.name = sub_category_json.get("name")
        sub_category_object.parentcategoryid = sub_category_json.get("parentcategoryid")
        sub_category_object.parentsubcategoryid = sub_category_json.get("parentsubcategoryid")
        sub_category_object.description = sub_category_json.get("description")
        sub_category_object.imageurl = sub_category_json.get("imageurl")

        sub_category_service: SubCategoryService = SubCategoryService()
        sub_category_object = sub_category_service.delete(sub_category_object)

        return self.send_response(sub_category_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        sub_category_service: SubCategoryService = SubCategoryService()
        data = sub_category_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        sub_category_service: SubCategoryService = SubCategoryService()
        data = sub_category_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        sub_category_service: SubCategoryService = SubCategoryService()
        data = sub_category_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        sub_category_service: SubCategoryService = SubCategoryService()
        data = sub_category_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        sub_category_service: SubCategoryService = SubCategoryService()
        data = sub_category_service.get_list_object_paginated(params)
        return self.send_response(data)
