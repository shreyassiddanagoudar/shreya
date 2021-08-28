"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from examsystemapp.repository.base_repository import BaseRepository
from django.db import transaction
from examsystemapp.repository.transaction_repository import TransactionRepository
from examsystemapp.repository.normal_repository import NormalRepository
from examsystemapp.utils.constants.constants import ErrorCodes

from examsystemapp.utils.helpers.request_helper import ParamsObject


class BaseService:

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        # If callee is not the transaction owner then, callee cannot commit or rollback the transaction
        self.is_transaction_owner = is_transaction_owner

        self.base_repository = BaseRepository()
        self.transaction_repo = TransactionRepository()
        self.normal_repo = NormalRepository()
        self.general_error_code = ErrorCodes.GENERAL_ERROR
        self.ext_params = ext_params
        self.event_type = event_type

    def begin_transaction(self):
        if self.is_transaction_owner:
            if transaction.get_autocommit():
                transaction.set_autocommit(autocommit=False)

    def commit(self):
        if self.is_transaction_owner:
            transaction.commit()
            self.close_cursor()

    def rollback(self):
        if self.is_transaction_owner:
            transaction.rollback()
            self.close_cursor()

    def close_cursor(self):
        self.base_repository.close_cursor()

    """ All CRUD operation """

    def add(self, object):
        self.begin_transaction()
        self.pre_add(object)
        returned_object = self.add_data(object)
        returned_object = self.post_add(returned_object)

        self.commit()
        return returned_object

    def pre_add(self, object):
        pass

    def add_data(self, object):
        pass

    def post_add(self, object):
        return object

    def update(self, object):
        self.begin_transaction()
        self.pre_update(object)
        returned_object = self.update_data(object)
        returned_object = self.post_update(returned_object)
        self.commit()
        return returned_object

    def pre_update(self, object):
        pass

    def update_data(self, object):
        pass

    def post_update(self, object):
        return object

    def delete(self, object):
        self.begin_transaction()
        self.pre_delete(object)
        returned_object = self.delete_data(object)

        returned_object = self.post_delete(returned_object)
        self.commit()
        return self.post_delete(returned_object)

    def pre_delete(self, object):
        pass

    def delete_data(self, object):
        pass

    def post_delete(self, object):
        return object

    def get(self, params: ParamsObject):
        self.pre_get(params)
        data = self.get_data(params)

        return self.post_get(data)

    def pre_get(self, params):
        pass

    def get_data(self, params):
        pass

    def post_get(self, object):
        return object

    def get_list(self, params: ParamsObject):
        self.pre_get_list(params)
        data_list_objects = self.get_data_list(params)

        return self.post_get_list(data_list_objects)

    def pre_get_list(self, params):
        pass

    def get_data_list(self, params):
        pass

    def post_get_list(self, object):
        return object

    def execute_raw_sql(self, raq_sql):
        data = None
        self.begin_transaction()
        data = self.base_repository.execute_raw_sql(raq_sql)
        self.commit()
        return data

    def __get_data_direct(self, sp_name, params: ParamsObject, is_cacheable=True, cache_key_prefix="",
                          is_multiple_rs=False):
        data = None
        if params is None:
            params = []
        if is_multiple_rs:
            data = self.normal_repo.get_direct_multiple(sp_name, params.get_params_list())
        else:
            data = self.normal_repo.get_direct(sp_name, params.get_params_list())
        return data

    def get_direct(self, sp_name, params, is_cacheable=True, cache_key_prefix=""):
        return self.__get_data_direct(sp_name, params, is_cacheable, cache_key_prefix, False)

    def get_direct_multiple(self, sp_name, params, is_cacheable=True, cache_key_prefix=""):
        return self.__get_data_direct(sp_name, params, is_cacheable, cache_key_prefix, True)

    def __add_update_delete_direct(self, sp_name, params: ParamsObject, flag="ADD"):
        data = None
        if flag == "ADD":
            data = self.normal_repo.add_direct(sp_name, params.get_params_list())
        elif flag == "UPDATE":
            data = self.normal_repo.update_direct(sp_name, params.get_params_list())
        elif flag == "DELETE":
            data = self.normal_repo.delete_direct(sp_name, params.get_params_list())
        else:
            pass
        return data

    def __add_update_delete_direct_transactional(self, sp_name, params: ParamsObject, flag="ADD"):
        data = None
        self.begin_transaction()
        if flag == "ADD":
            data = self.transaction_repo.add_direct(sp_name, params.get_params_list())
        elif flag == "UPDATE":
            data = self.transaction_repo.update_direct(sp_name, params.get_params_list())
        elif flag == "DELETE":
            data = self.transaction_repo.delete_direct(sp_name, params.get_params_list())
        else:
            pass
        self.commit()
        return data

    def add_direct(self, sp_name, params):
        return self.__add_update_delete_direct(sp_name, params, "ADD")

    def update_direct(self, sp_name, params):
        return self.__add_update_delete_direct(sp_name, params, "UPDATE")

    def delete_direct(self, sp_name, params):
        return self.__add_update_delete_direct(sp_name, params, "DELETE")

    def add_direct_transactional(self, sp_name, params):
        return self.__add_update_delete_direct_transactional(sp_name, params, "ADD")

    def update_direct_transactional(self, sp_name, params):
        return self.__add_update_delete_direct_transactional(sp_name, params, "UPDATE")

    def delete_direct_transactional(self, sp_name, params):
        return self.__add_update_delete_direct_transactional(sp_name, params, "DELETE")

    def get_object(self, params: ParamsObject):
        data = None
        self.pre_get_object(params)
        data = self.get_data_object(params)
        return self.post_get_object(data)

    def pre_get_object(self, params):
        pass

    def get_data_object(self, params):
        pass

    def post_get_object(self, object):
        return object

    def get_list_object(self, params: ParamsObject):
        data = None
        self.pre_get_list_object(params)
        data = self.get_data_list_object(params)

        return self.post_get_list_object(data)

    def get_data_list_object(self, params):
        pass

    def pre_get_list_object(self, params):
        pass

    def post_get_list_object(self, object):
        return object

    def get_list_object_paginated(self, params: ParamsObject):
        data = None
        self.pre_get_list_object_paginated(params)
        data = self.get_data_list_object_paginated(params)

        return self.post_get_list_object_paginated(data)

    def get_data_list_object_paginated(self, params):
        pass

    def pre_get_list_object_paginated(self, params):
        pass

    def post_get_list_object_paginated(self, object):
        return object
