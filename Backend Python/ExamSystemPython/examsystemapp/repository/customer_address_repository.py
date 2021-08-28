"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.customer_address import CustomerAddressModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CustomerAddressRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CustomerAddressModel):
        self.sp_name = "sCustomerAddressAdd"
        list_params = [object.customeraddressid,object.customerid,object.add1,object.add2,object.add3,object.cityid,object.stateid,object.pincode]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        customer_address_model: CustomerAddressModel = object
        customer_address_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return customer_address_model

    def pre_update(self, object: CustomerAddressModel):
        self.sp_name = "sCustomerAddressUpdate"
        list_params = [object.customeraddressid,object.customerid,object.add1,object.add2,object.add3,object.cityid,object.stateid,object.pincode]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        customer_address_model: CustomerAddressModel = object
        customer_address_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return customer_address_model

    def pre_delete(self, object: CustomerAddressModel):
        self.sp_name = "sCustomerAddressDelete"
        list_params = [object.customeraddressid,object.customerid,object.add1,object.add2,object.add3,object.cityid,object.stateid,object.pincode]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        customer_address_model: CustomerAddressModel = object
        customer_address_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return customer_address_model

    def pre_get(self, params):
        self.sp_name = "sCustomerAddressGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            customer_address_model: CustomerAddressModel = CustomerAddressModel()
            for each_tuple in cursor_object.get_data():
                customer_address_model.customeraddressid = each_tuple[0]
                customer_address_model.customerid = each_tuple[1]
                customer_address_model.add1 = each_tuple[2]
                customer_address_model.add2 = each_tuple[3]
                customer_address_model.add3 = each_tuple[4]
                customer_address_model.cityid = each_tuple[5]
                customer_address_model.stateid = each_tuple[6]
                customer_address_model.pincode = each_tuple[7]

            return customer_address_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCustomerAddressGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                customer_address_model: CustomerAddressModel = CustomerAddressModel()
                customer_address_model.customeraddressid = each_tuple[0]
                customer_address_model.customerid = each_tuple[1]
                customer_address_model.add1 = each_tuple[2]
                customer_address_model.add2 = each_tuple[3]
                customer_address_model.add3 = each_tuple[4]
                customer_address_model.cityid = each_tuple[5]
                customer_address_model.stateid = each_tuple[6]
                customer_address_model.pincode = each_tuple[7]

                list_data.append(customer_address_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCustomerAddressObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCustomerAddressObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCustomerAddressObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None

    def get_list_customer_adderss_by_id(self, params):
        # self.sp_name = "sGetCustomerAddress"
        # self.params_list = params.get_params_list() 
        return self.get_direct("sGetCustomerAddress", params.get_params_list())
        


    
              
