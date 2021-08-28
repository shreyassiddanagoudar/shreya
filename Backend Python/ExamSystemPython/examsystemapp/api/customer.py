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
from examsystemapp.models.customer import CustomerModel
from examsystemapp.services.customer_service import CustomerService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Customer(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        customer_json = json.loads(request.POST.get("customer_json"))

        customer_object: CustomerModel = CustomerModel()
        customer_object.customerid = customer_json.get("customerid")
        customer_object.email = customer_json.get("email")
        customer_object.phone = customer_json.get("phone")
        customer_object.name = customer_json.get("name")
        customer_object.password = customer_json.get("password")

        customer_service: CustomerService = CustomerService()
        customer_object = customer_service.add(customer_object)

        return self.send_response(customer_object)

    def update(self, request: HttpRequest):
        customer_json = json.loads(request.POST.get("customer_json"))

        customer_object: CustomerModel = CustomerModel()
        customer_object.customerid = customer_json.get("customerid")
        customer_object.email = customer_json.get("email")
        customer_object.phone = customer_json.get("phone")
        customer_object.name = customer_json.get("name")
        customer_object.password = customer_json.get("password")

        customer_service: CustomerService = CustomerService()
        customer_object = customer_service.update(customer_object)

        return self.send_response(customer_object)

    def delete(self, request: HttpRequest):
        customer_json = json.loads(request.POST.get("customer_json"))

        customer_object: CustomerModel = CustomerModel()
        customer_object.customerid = customer_json.get("customerid")
        customer_object.email = customer_json.get("email")
        customer_object.phone = customer_json.get("phone")
        customer_object.name = customer_json.get("name")
        customer_object.password = customer_json.get("password")

        customer_service: CustomerService = CustomerService()
        customer_object = customer_service.delete(customer_object)

        return self.send_response(customer_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_service: CustomerService = CustomerService()
        data = customer_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_service: CustomerService = CustomerService()
        data = customer_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_service: CustomerService = CustomerService()
        data = customer_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_service: CustomerService = CustomerService()
        data = customer_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_service: CustomerService = CustomerService()
        data = customer_service.get_list_object_paginated(params)
        return self.send_response(data)

    def customer_authentication(self, request: HttpRequest):
        params = [
            {"phone_num": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)},
            {"password": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')},
            {"session_id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}

        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_service: CustomerService = CustomerService()
        data = customer_service.customer_authentication(params)
        return self.send_response(data)
