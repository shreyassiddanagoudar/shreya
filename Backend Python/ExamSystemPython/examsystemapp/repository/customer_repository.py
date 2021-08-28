"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.customer import CustomerModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject
from examsystemapp.repository.customer_address_repository import CustomerAddressRepo
from examsystemapp.repository.cart_repository import CartRepo

class CustomerRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CustomerModel):
        self.sp_name = "sCustomerAdd"
        list_params = [object.customerid,object.email,object.phone,object.name,object.password]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        customer_model: CustomerModel = object
        customer_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return customer_model

    def pre_update(self, object: CustomerModel):
        self.sp_name = "sCustomerUpdate"
        list_params = [object.customerid,object.email,object.phone,object.name,object.password]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        customer_model: CustomerModel = object
        customer_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return customer_model

    def pre_delete(self, object: CustomerModel):
        self.sp_name = "sCustomerDelete"
        list_params = [object.customerid,object.email,object.phone,object.name,object.password]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        customer_model: CustomerModel = object
        customer_model.id = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return customer_model

    def pre_get(self, params):
        self.sp_name = "sCustomerGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            customer_model: CustomerModel = CustomerModel()
            for each_tuple in cursor_object.get_data():
                customer_model.customerid = each_tuple[0]
                customer_model.email = each_tuple[1]
                customer_model.phone = each_tuple[2]
                customer_model.name = each_tuple[3]
                customer_model.password = each_tuple[4]

            return customer_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCustomerGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                customer_model: CustomerModel = CustomerModel()
                customer_model.customerid = each_tuple[0]
                customer_model.email = each_tuple[1]
                customer_model.phone = each_tuple[2]
                customer_model.name = each_tuple[3]
                customer_model.password = each_tuple[4]

                list_data.append(customer_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCustomerObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCustomerObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCustomerObjectGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None

    def customer_authentication(self, params: ParamsObject):
        # return params.get_params_list()
        return self.get_direct("sCustomerAuthenticate", params.get_params_list())

    def customer_authentication(self, params: ParamsObject):
        # return params.get_params_list()
        #return self.get_direct("sCustomerAuthenticate", params.get_params_list())
         # return params.get_params_list()
        # return params.get_params_list()
        customer = self.get_direct("sCustomerAuthenticate", params.get_params_list())

        if customer is None:
            return None
        
        if len(customer) <= 0:
            return None
        
        customer = customer[0]

        # # # Call Cutomer Address Repo
        customer_address_repo : CustomerAddressRepo = CustomerAddressRepo()
        params: ParamsObject = ParamsObject()
        params.set_params_list([customer.get('CustomerID')])
        address = customer_address_repo.get_list_customer_adderss_by_id(params)
        #print(address)

        # Call Cart Repo
        
        cart_params: ParamsObject = ParamsObject()
        cart_params.set_params_list([params.get_params_dict().get("sessionid"), customer.get('CustomerID')])
       
        cart_repo:CartRepo = CartRepo()
        cart = cart_repo.get_data_object(cart_params)

        customer['address'] = address
        customer['cart'] =cart

        return customer

            
