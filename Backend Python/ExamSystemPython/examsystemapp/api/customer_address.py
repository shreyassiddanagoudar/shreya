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
from examsystemapp.models.customer_address import CustomerAddressModel
from examsystemapp.services.customer_address_service import CustomerAddressService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class CustomerAddress(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        customer_address_json = json.loads(request.POST.get("customer_address_json"))

        customer_address_object: CustomerAddressModel = CustomerAddressModel()
        customer_address_object.customeraddressid = customer_address_json.get("customeraddressid")
        customer_address_object.customerid = customer_address_json.get("customerid")
        customer_address_object.add1 = customer_address_json.get("add1")
        customer_address_object.add2 = customer_address_json.get("add2")
        customer_address_object.add3 = customer_address_json.get("add3")
        customer_address_object.cityid = customer_address_json.get("cityid")
        customer_address_object.stateid = customer_address_json.get("stateid")
        customer_address_object.pincode = customer_address_json.get("pincode")

        customer_address_service: CustomerAddressService = CustomerAddressService()
        customer_address_object = customer_address_service.add(customer_address_object)

        return self.send_response(customer_address_object)

    def update(self, request: HttpRequest):
        customer_address_json = json.loads(request.POST.get("customer_address_json"))

        customer_address_object: CustomerAddressModel = CustomerAddressModel()
        customer_address_object.customeraddressid = customer_address_json.get("customeraddressid")
        customer_address_object.customerid = customer_address_json.get("customerid")
        customer_address_object.add1 = customer_address_json.get("add1")
        customer_address_object.add2 = customer_address_json.get("add2")
        customer_address_object.add3 = customer_address_json.get("add3")
        customer_address_object.cityid = customer_address_json.get("cityid")
        customer_address_object.stateid = customer_address_json.get("stateid")
        customer_address_object.pincode = customer_address_json.get("pincode")

        customer_address_service: CustomerAddressService = CustomerAddressService()
        customer_address_object = customer_address_service.update(customer_address_object)

        return self.send_response(customer_address_object)

    def delete(self, request: HttpRequest):
        customer_address_json = json.loads(request.POST.get("customer_address_json"))

        customer_address_object: CustomerAddressModel = CustomerAddressModel()
        customer_address_object.customeraddressid = customer_address_json.get("customeraddressid")
        customer_address_object.customerid = customer_address_json.get("customerid")
        customer_address_object.add1 = customer_address_json.get("add1")
        customer_address_object.add2 = customer_address_json.get("add2")
        customer_address_object.add3 = customer_address_json.get("add3")
        customer_address_object.cityid = customer_address_json.get("cityid")
        customer_address_object.stateid = customer_address_json.get("stateid")
        customer_address_object.pincode = customer_address_json.get("pincode")

        customer_address_service: CustomerAddressService = CustomerAddressService()
        customer_address_object = customer_address_service.delete(customer_address_object)

        return self.send_response(customer_address_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_address_service: CustomerAddressService = CustomerAddressService()
        data = customer_address_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_address_service: CustomerAddressService = CustomerAddressService()
        data = customer_address_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_address_service: CustomerAddressService = CustomerAddressService()
        data = customer_address_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_address_service: CustomerAddressService = CustomerAddressService()
        data = customer_address_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_address_service: CustomerAddressService = CustomerAddressService()
        data = customer_address_service.get_list_object_paginated(params)
        return self.send_response(data)

    def get_list_customer_adderss_by_id(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT, default=1)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        customer_address_service: CustomerAddressService = CustomerAddressService()
        data = customer_address_service.get_list_customer_adderss_by_id(params)
        return self.send_response(data)
