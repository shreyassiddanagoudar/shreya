"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from examsystemapp.repository.base_repository import BaseRepository
from django.db import transaction
from examsystemapp.utils.cache_manager.cachable import ICachable
from examsystemapp.utils.cache_manager.cache_manager import RedisCacheManager
from examsystemapp.repository.transaction_repository import TransactionRepository
from examsystemapp.repository.normal_repository import NormalRepository
from examsystemapp.utils.exception_handling.exception import KaroException, DatabaseException, CacheException, \
    ValidationException
from examsystem.settings import base
from examsystemapp.utils.helpers.general_helper import Validation
from examsystemapp.utils.helpers.logging_helper import LoggingHelper
from examsystemapp.utils.constants.constants import ErrorCodes
import threading

from examsystemapp.utils.helpers.request_helper import ParamsObject


class BaseService:

    def __init__(self, ext_params={}, is_transaction_owner=True, event_type=None):
        # If callee is not the transaction owner then, callee cannot commit or rollback the transaction
        self.is_transaction_owner = is_transaction_owner

        self.base_repository = BaseRepository()
        self.cache_manager = RedisCacheManager()
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

    """
    Cache helper methods
    """

    def get_from_cache(self, cache_key):
        return self.cache_manager.get_cached(cache_key)

    def get_object_from_cache(self, cache_key):
        return self.cache_manager.get_object_from_cache(cache_key)

    def put_in_cache(self, cache_key, data):
        return self.cache_manager.put_in_cache(cache_key, data)

    def put_object_in_cache(self, cache_key, data):
        return self.cache_manager.put_object_in_cache(cache_key, data)

    def has_key(self, cache_key):
        return self.cache_manager.has_key(cache_key)

    def generate_cache_key(self, object, params):
        return self.cache_manager.get_cache_key(object, params)

    def invalidate_cache(self, cache_key):
        self.cache_manager.invalidate_cache(cache_key)

    def invalidate_cache_by_prefix(self, prefix):
        self.cache_manager.invalidate_cache_by_prefix(prefix)

    def clear_cache(self):
        self.cache_manager.clear_cache()

    def __cache_add_or_update_or_delete(self, cache_key, id, object, flag="ADD"):
        """
        :description: This method facilitates the callee to add/update/delete the object from the cache
                      Run this in a separate thread, so that it will nnot block the current running thread
        :param cache_key: Key to the cache
        :param id: Object ID (Will be concatenated while generating the cache key)
        :param object: Actual Object
        :param flag: ADD/UPDATE/DELETE
        :return: True or False
        """
        lst = []
        lst.append(str(id))
        params_object: ParamsObject = ParamsObject()
        params_object.set_params_list(lst)
        prefix = cache_key
        cache_key = self.generate_cache_key(cache_key, params_object)
        if flag == "DELETE":
            self.invalidate_cache(cache_key)
        else:
            if object is not None:
                self.put_object_in_cache(cache_key, object)
        self.invalidate_cache(prefix + ":")
        return True

    def __is_object_valid(self, object, type="ADD"):
        validation_object: Validation = object.is_valid(type, self.event_type)
        if not validation_object.is_valid:
            raise ValidationException(ErrorCodes.VALIDATION_ERROR, validation_object.validation_message,
                                      validation_object.validation_object)

    """ All CRUD operation """

    def add(self, object):
        """
        :description: This method facilitates the add facility to the user for an object
                      After adding, if the object is cacheable then this method adds the object in to the                         cache
        :param object: Actual object (Model)
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        returned_object = None
        try:
            self.__is_object_valid(object, "ADD")
            self.begin_transaction()
            self.pre_add(object)
            returned_object = self.add_data(object)

            if isinstance(self, ICachable):
                cache_key = self.get_cache_key()
                id = returned_object.get_id()
                t = threading.Thread(target=self.__cache_add_or_update_or_delete,
                                     args=(cache_key, id, returned_object, "ADD"))
                t.start()

            returned_object = self.post_add(returned_object)
            self.commit()
            return returned_object
        except ValidationException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            returned_object = self.post_add(returned_object)
            self.commit()
            return returned_object
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)

    def pre_add(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything before adding the object
        :param object:  Actual object (Model)
        :return:
        """
        pass

    def add_data(self, object):
        """
        :Description: This method should be overridden in the child class to class add the object
        :param object: Actual object (Model)
        :return: Actual object (Model)
        """
        pass

    def post_add(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after adding the object
        :param object: Actual object (Model)
        :return: Actual object (Model)
        """
        return object

    def update(self, object):
        """
        :description: This method facilitates the update facility to the user for an object
                        This updates the complete object. Partial updated cannot be done using this method
                        After updating, if the object is cacheable then this method updates the object in the cache
        :param object: Actual object (Model)
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        returned_object = None
        try:
            self.__is_object_valid(object, "UPDATE")
            self.begin_transaction()
            self.pre_update(object)
            returned_object = self.update_data(object)

            if isinstance(self, ICachable):
                cache_key = self.get_cache_key()
                id = returned_object.get_id()
                t = threading.Thread(target=self.__cache_add_or_update_or_delete,
                                     args=(cache_key, id, returned_object, "UPDATE"))
                t.start()

            returned_object = self.post_update(returned_object)
            self.commit()
            return returned_object
        except ValidationException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            returned_object = self.post_update(returned_object)
            self.commit()
            return returned_object
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)

    def pre_update(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything before updating the object
        :param object: Actual object (Model)
        :return: Actual object (Model)
        """
        pass

    def update_data(self, object):
        """
        :Description: This method should be overridden in the child to facilitate the object update
        :param object: Actual object (Model)
        :return: Actual updated object (Model)
        """
        pass

    def post_update(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after updating the object
        :param object: Actual object (Model)
        :return: Actual updated object (Model)
        """
        return object

    def delete(self, object):
        """
        :description: This method facilitates the delete facility to the user for an object
            After deleting, if the object is cacheable then this method removes the object from the cache
        :param object: Actual object (Model)
        :return: Actual deleted object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        returned_object = None
        try:
            self.__is_object_valid(object, "DELETE")
            self.begin_transaction()
            self.pre_delete(object)
            returned_object = self.delete_data(object)

            if isinstance(self, ICachable):
                cache_key = self.get_cache_key()
                id = returned_object.get_id()
                t = threading.Thread(target=self.__cache_add_or_update_or_delete,
                                     args=(cache_key, id, returned_object, "DELETE"))
                t.start()

            returned_object = self.post_delete(returned_object)
            self.commit()
            return self.post_delete(returned_object)
        except ValidationException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            returned_object = self.post_delete(returned_object)
            self.commit()
            return returned_object
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)

    def pre_delete(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything before deleting the object
        :param object: Actual object (Model)
        :return: Actual deleted object (Model)
        """
        pass

    def delete_data(self, object):
        """
        :Description: This method should be overridden in the child  to process the delete operation for the object
        :param object: Actual object (Model)
        :return: Actual deleted object (Model)
        """
        pass

    def post_delete(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after deleting the object
        :param object: Actual object (Model)
        :return: Actual deleted object (Model)
        """
        return object

    def get(self, params: ParamsObject):
        """
        :description: This method facilitates ccallee to get the single object by ID.
                      If the Object is cacheable then, this method checks the cache first and then
                      id object is in cache it returns else gets the object from database and
                      puts in the cache.
        :param params: ParamsObject
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data = None
        try:

            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache
            self.pre_get(params)
            if isinstance(self, ICachable):
                cache_key = self.generate_cache_key(self.get_cache_key(), params)
                data = self.get_object_from_cache(cache_key)
                if data is None:
                    data = self.get_data(params)
                    if data is not None:
                        self.put_object_in_cache(cache_key, data)
            else:
                data = self.get_data(params)

            return self.post_get(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get(data)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def pre_get(self, params):
        """
        :Description: This method should be overridden in the child if child needs to process anything before getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def get_data(self, params):
        """
        :Description: This method should be overridden in the child to process the get operation
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def post_get(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        return object

    def get_data_by_id_from_db(self, params: ParamsObject):
        """
        :description: This method facilitates the callee to get the actual object from the database always
                      If the object is cacheable the this method puts the object in cahce with prefix and ID
                      To facilate this object should expose the get service, as this uses get                                     service
        :param params:
        :return:
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data = None
        try:
            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache if is cacheable
            self.pre_get(params)

            # List of objects
            data = self.get_data(params)

            # Do this in a separate thread. So that it wont block the current thread
            if isinstance(self, ICachable):
                cache_key = self.get_cache_key()
                id = data.get_id()
                t = threading.Thread(target=self.__cache_add_or_update_or_delete,
                                     args=(cache_key, id, data, "ADD"))
                t.start()

            return self.post_get(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get(data)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    # Run this on a seperate thread
    def put_data_object_in_cache(self, data_object, cache_prefix=""):
        """
        :description: This puts the object (Model) in the cache. Run this in a separate thread so that it                         wont block the main thread operation
        :param data_object: Actual Object (Model)
        :param cache_prefix: This is a cache prefix. Cache manager will append the id with this prefix
        :return: Void
        """
        if data_object is not None:
            for each_object in data_object:
                if each_object is not None:
                    lst = [str(each_object.get_id())]
                    params_object = ParamsObject()
                    params_object.set_params_list(lst)
                    cache_key = self.generate_cache_key(cache_prefix, params_object)
                    self.cache_manager.put_object_in_cache(cache_key, each_object)

    def get_data_list_by_ids_from_db(self, params: ParamsObject):
        """
        :description: This method facilitates the callee to get the actual object from the database always
                      If the object is cacheable the this method puts the object in cahce with prefix and ID
                      To facilate this object shold expose the get_list service, as this uses get_list                            service
        :param params:
        :return:
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data = None
        try:
            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache if is cacheable
            self.pre_get_list(params)

            # List of objects
            data = self.get_data_list(params)

            # Do this in a separate thread. So that it wont block the current thread
            if isinstance(self, ICachable):
                cache_prefix = self.get_cache_key()
                t1 = threading.Thread(target=self.put_data_object_in_cache, args=(data, cache_prefix))
                t1.start()
                # for (_dict, _object) in zip(data.get_list_dict(), data.get_list_objects()):
                #     lst = [str(_object.get_id())]
                #     cache_key = self.generate_cache_key(cache_prefix, {"list": lst})
                #     self.cache_manager.put_in_cache(cache_key, _dict)

            return self.post_get_list(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get_list(data)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def get_list(self, params: ParamsObject):
        """
        :description: This method facilitates the callee to get the list of objects (Model) either from cache
                      or from the database.
                      This uses get_data_list_by_ids_from_db to get the list objects from the database.
                      This method checks the ids which are in cache and the other ids which are not in cache
                      will get from the database and puts in cache if the object is cacheable
        :param params: ParamsObject (Will be having the list of ids)
        :return: List of actual objects (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data_list_objects = []
        try:

            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache
            self.pre_get_list(params)

            if params.get_params_list() is None or len(params.get_params_list()) <= 0:
                lst = list()
                lst.append("")
                params.set_params_list(lst)

                if isinstance(self, ICachable):
                    cache_key = self.generate_cache_key(self.get_cache_key(), params)
                    data_list_objects = self.get_object_from_cache(cache_key)
                    if data_list_objects is None:
                        data_list_objects = self.get_data_list(params)
                        if data_list_objects is not None:
                            self.put_object_in_cache(cache_key, data_list_objects)
                else:
                    data_list_objects = self.get_data_list(params)
            else:
                str_ids = params.get_params_list()[0]
                list_ids = str_ids.split(",")

                if isinstance(self, ICachable):
                    list_objects = self.cache_manager.get_cached_objects_by_ids(self.get_cache_key(), list_ids)

                    if len(list_objects) > 0:
                        data_list_objects.extend(list_objects)

                    exists_keys = [str(each_object.get_id()) for each_object in list_objects]
                    not_in_cache = [x for x in list_ids if x not in exists_keys]

                    if len(not_in_cache) > 0:
                        list_str = ','.join(str(e) for e in not_in_cache)
                        lst = [list_str]

                        params_object = ParamsObject()
                        params_object.set_params_list(lst)

                        data_not_in_cache = self.get_data_list_by_ids_from_db(params_object)
                        if data_not_in_cache is not None:
                            data_list_objects.extend(data_not_in_cache)
                else:
                    data_list_objects = self.get_data_list(params)

            return self.post_get_list(data_list_objects)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get_list(data_list_objects)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def pre_get_list(self, params):
        """
        :Description: This method should be overridden in the child if child needs to process anything after                      getting the object list
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def get_data_list(self, params):
        """
        :Description: This method should be overridden in the child to process to get object list
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def post_get_list(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process                                     anything after getting the object list
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        return object

    def execute_raw_sql(self, raq_sql):
        """
        :Description: This method facilitate the callee to call the raw sql
        :param raw_sql: String (raq_sql)
        :return: list of dictionary
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", raq_sql)
        data = None
        try:
            self.begin_transaction()
            data = self.base_repository.execute_raw_sql(raq_sql)
            self.commit()
        except DatabaseException as ex:
            # Log the exception if debug is true
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        return data

    """
     ORM Specific CRUD  
    """

    def add_using_orm(self, object):
        """
        :description: This method facilitates the callee to use ORM to add the object
        :param object: Model Object
        :return: Model Object
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            return self.add_using_orm_data(object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            return None

    def add_using_orm_data(self, object):
        """
        :description: This method should be overridden to process the add operation
        :param object: Model Object
        :return: Model Object
        """
        pass

    def update_using_orm(self, object):
        """
        :description: This method facilitates the callee to use ORM to update the object
        :param object: Model Object
        :return: Model Object
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            return self.update_using_orm_data(object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            return None

    def update_using_orm_data(self, request):
        """
        :description: This method should be overridden to process the update operation
        :param object: Model Object
        :return: Model Object
        """
        pass

    def delete_using_orm(self, object):
        """
        :description: This method facilitates the callee to use ORM to delete the object
        :param object: Model Object
        :return: Model Object
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            return self.delete_using_orm_data(object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            return None

    def delete_using_orm_data(self, request):
        """
        :description: This method should be overridden to process the delete operation
        :param object: Model Object
        :return: Model Object
        """
        pass

    def get_using_orm(self, object):
        """
        :description: This method facilitates the callee to use ORM to get the object
        :param object: Model Object
        :return: Model Object
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            return self.get_using_orm_data(object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            return None

    def get_using_orm_data(self, object):
        """
        :description: This method should be overridden to process the get operation
        :param object: Model Object
        :return: Model Object
        """
        pass

    def __get_data_direct(self, sp_name, params: ParamsObject, is_cacheable=True, cache_key_prefix="",
                          is_multiple_rs=False):
        """
        :decription: This is a private method. SHould not be called from any other place
                     This method facilitates to get the data as list of dictionary from the database
                     This first checks the cache and then gets the data from the database if the data is not
                     in cache and also callee says this is cacheable
        :param sp_name: Procedure name to ca;;
        :param params: ParamsObject (Will have the list of parameters to pass to SP)
        :param is_cacheable: True or False
        :param cache_key_prefix: Prefix to the cache Key
        :param is_multiple_rs: True of False
        :return: List of Dictionary (Whatever is coming from the database as is)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", {"sp": sp_name, "params": params.get_params_list()})
        data = None
        if params is None:
            params = []
        try:
            if is_cacheable:
                cache_key = self.generate_cache_key(cache_key_prefix, params)
                data = self.get_from_cache(cache_key)
                if data is None or data == "":
                    if is_multiple_rs:
                        data = self.normal_repo.get_direct_multiple(sp_name, params.get_params_list())
                    else:
                        data = self.normal_repo.get_direct(sp_name, params.get_params_list())
                    self.put_in_cache(cache_key, data)
            else:
                if is_multiple_rs:
                    data = self.normal_repo.get_direct_multiple(sp_name, params.get_params_list())
                else:
                    data = self.normal_repo.get_direct(sp_name, params.get_params_list())
            return data
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            self.rollback()
            return data
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            raise KaroException(self.general_error_code, str(ex1), None)

    def get_direct(self, sp_name, params, is_cacheable=True, cache_key_prefix=""):
        """
        :description: This calls the __get_data_direct_ to process the cache and getting the data
                      This should always be used when the resultset is single
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to the procedure)
        :param is_cacheable:  True or False
        :param cache_key_prefix: Prefix to cache key
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__get_data_direct(sp_name, params, is_cacheable, cache_key_prefix, False)

    def get_direct_multiple(self, sp_name, params, is_cacheable=True, cache_key_prefix=""):
        """
        :description: This calls the __get_data_direct_ to process the cache and getting the data
                      This should always be used when the resultset is multiple
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to the procedure)
        :param is_cacheable:  True or False
        :param cache_key_prefix: Prefix to cache key
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__get_data_direct(sp_name, params, is_cacheable, cache_key_prefix, True)

    """
    This is a private method and should not access directly for the other classes
    This method facilitates callee to call the SP directly for add/update/delete without transaction at repo level
    Returns the data returned by the Database Repository
    """

    def __add_update_delete_direct(self, sp_name, params: ParamsObject, flag="ADD"):
        """
        :description: This method facilitates the callee to add/update/delete the data from the database.
                      This does not provide the transaction. Callee needs to handle the transaction
                      To use the transaction use __add_update_delete_direct_transactional rather
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :param flag: ADD/UPDATE/DELETE
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", {"sp": sp_name, "params": params.get_params_list()})
        data = None
        try:
            if flag == "ADD":
                data = self.normal_repo.add_direct(sp_name, params.get_params_list())
            elif flag == "UPDATE":
                data = self.normal_repo.update_direct(sp_name, params.get_params_list())
            elif flag == "DELETE":
                data = self.normal_repo.delete_direct(sp_name, params.get_params_list())
            else:
                pass

        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return data
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            raise KaroException(self.general_error_code, str(ex1), None)
        return data

    def __add_update_delete_direct_transactional(self, sp_name, params: ParamsObject, flag="ADD"):
        """
        :description: This method facilitates the callee to add/update/delete the data from the database.
                      This method facilitates the transaction
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :param flag: ADD/UPDATE/DELETE
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", {"sp": sp_name, "params": params.get_params_list()})
        data = None
        try:
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
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return data
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)

    def add_direct(self, sp_name, params):
        """
        :description: This method facilitates the callee to add the data into the database.
                       This does not provide the transaction. Callee needs to handle the transaction
                       To use the transaction use add_direct_transactional rather
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__add_update_delete_direct(sp_name, params, "ADD")

    def update_direct(self, sp_name, params):
        """
        :description: This method facilitates the callee to update the data in the database.
                      This does not provide the transaction. Callee needs to handle the transaction
                      To use the transaction use update_direct_transactional rather
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__add_update_delete_direct(sp_name, params, "UPDATE")

    def delete_direct(self, sp_name, params):
        """
        :description: This method facilitates the callee to delete the data from the database.
                      This does not provide the transaction. Callee needs to handle the transaction
                      To use the transaction use delete_direct_transactional rather
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__add_update_delete_direct(sp_name, params, "DELETE")

    def add_direct_transactional(self, sp_name, params):
        """
        :description: This method facilitates the callee to add the data into database.
                      This provides the transaction
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__add_update_delete_direct_transactional(sp_name, params, "ADD")

    def update_direct_transactional(self, sp_name, params):
        """
        :description: This method facilitates the callee to updates the data in the database.
                      This provides the transaction
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__add_update_delete_direct_transactional(sp_name, params, "UPDATE")

    def delete_direct_transactional(self, sp_name, params):
        """
        :description: This method facilitates the callee to deletes the data from the database.
                      This provides the transaction
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to send to procedure)
        :return: List of dictionary (Whatever is coming from the database as is)
        """
        return self.__add_update_delete_direct_transactional(sp_name, params, "DELETE")

    def get_common(self, sp_name, params: ParamsObject, is_cacheable=False, cache_key_prefix=""):
        """
        :description: This method facilitates the callee to call the Procedure directly which always returns                      the list of ids
                      using this ids this method calls the  get_data_list_by_ids_from_db to get the data which
                      are not in the cache if the callee says this is cacheable
                      This methos should be used only for single result set
                      For Multiple result set use get_common_multiple_rs
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to call the procedure)
        :param is_cacheable: True or False
        :param cache_key_prefix: Prefix will appended with parameters while generating the cache key
        :return: List of dictionary (Whatever is coming from the database as is). Which id concatenated ids
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", {"sp": sp_name, "params": params.get_params_list()})
        data_list_objects = []
        data = None
        try:
            if is_cacheable:
                cache_key = self.generate_cache_key(cache_key_prefix, params)
                data = self.cache_manager.get_object_from_cache(cache_key)
                if data is None:
                    data = self.normal_repo.get_direct(sp_name, params.get_params_list())
                    if data is not None:
                        self.cache_manager.put_object_in_cache(cache_key, data)
            else:
                data = self.normal_repo.get_direct(sp_name, params.get_params_list())

            id_key_alias = next(iter(data[0]))
            str_ids = data[0].get(id_key_alias)
            if str_ids == "" or str_ids is None:
                return None
            list_ids = str_ids.split(",")

            if isinstance(self, ICachable):
                list_objects = self.cache_manager.get_cached_objects_by_ids(self.get_cache_key(), list_ids)

                if len(list_objects) > 0:
                    data_list_objects.extend(list_objects)

                exists_keys = [str(each_object.get_id()) for each_object in list_objects]
                not_in_cache = [x for x in list_ids if x not in exists_keys]

                if len(not_in_cache) > 0:
                    list_str = ','.join(str(e) for e in not_in_cache)
                    lst = [list_str]

                    params_object = ParamsObject()
                    params_object.set_params_list(lst)

                    data_not_in_cache = self.get_data_list_by_ids_from_db(params_object)
                    if data_not_in_cache is not None:
                        data_list_objects.extend(data_not_in_cache)
            else:
                _params: ParamsObject = ParamsObject()
                _params.set_params_list(list_ids)
                data_list_objects = self.get_data_list(_params)
                data_list_objects = self.post_get_list(data_list_objects)

            return data_list_objects
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return data_list_objects
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex), None)
        finally:
            self.close_cursor()

    def get_common_multiple_rs(self, sp_name, params, is_cacheable=False, cache_key_prefix=""):
        """
        :description: This method facilitates the callee to call the Procedure directly which always returns                      list of ids
                      using this ids this method calls the  get_data_list_by_ids_from_db to get the data which
                      are not in the cache if the callee says this is cacheable
                      This methos should be used only for single result set
                      This method should be used to get the multiple result set always.
        :param sp_name: Procedure name to call
        :param params: ParamsObject (Will have the list of parameters to call the procedure)
        :param is_cacheable: True or False
        :param cache_key_prefix: Prefix will appended with parameters while generating the cache key
        :return: List of dictionary (Whatever is coming from the database as is). Which id concatenated ids
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", {"sp": sp_name, "params": params.get_params_list()})
        data_list_objects = []
        first_rs_dict = None
        data = None
        try:
            if is_cacheable:
                cache_key = self.generate_cache_key(cache_key_prefix, params)
                data = self.cache_manager.get_object_from_cache(cache_key)
                if data is None:
                    data = self.normal_repo.get_direct_multiple(sp_name, params.get_params_list())
                    if data is not None:
                        self.cache_manager.put_object_in_cache(cache_key, data)
            else:
                data = self.normal_repo.get_direct_multiple(sp_name, params.get_params_list())

            first_rs_dict = data[0].get("pages")

            id_key_alias = next(iter(data[0].get("data")[0]))
            str_ids = data[0].get("data")[0].get(id_key_alias)
            if str_ids == "" or str_ids is None:
                return None
            list_ids = str_ids.split(",")

            if isinstance(self, ICachable):
                list_objects = self.cache_manager.get_cached_objects_by_ids(self.get_cache_key(), list_ids)

                if len(list_objects) > 0:
                    data_list_objects.extend(list_objects)

                exists_keys = [str(each_object.get_id()) for each_object in list_objects]
                not_in_cache = [x for x in list_ids if x not in exists_keys]

                if len(not_in_cache) > 0:
                    list_str = ','.join(str(e) for e in not_in_cache)
                    lst = [list_str]

                    params_object = ParamsObject()
                    params_object.set_params_list(lst)

                    data_not_in_cache = self.get_data_list_by_ids_from_db(params_object)
                    if data_not_in_cache is not None:
                        data_list_objects.extend(data_not_in_cache)
            else:
                lst = []
                lst.append(str_ids)
                params_object = ParamsObject()
                params_object.set_params_list(lst)
                data_list_objects = self.get_data_list(params_object)

            multiple_rs_dict = dict()

            multiple_rs_dict["pages"] = first_rs_dict
            multiple_rs_dict["data"] = data_list_objects

            return multiple_rs_dict
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            multiple_rs_dict = dict()
            multiple_rs_dict[1] = first_rs_dict
            multiple_rs_dict[2] = data_list_objects
            return multiple_rs_dict
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex), None)
        finally:
            self.close_cursor()

    def get_object(self, params: ParamsObject):
        """
        :description: This method facilitates callee to get the single transactional object for any context.
                      If the Object is cacheable then, this method checks the cache first and then
                      id object is in cache it returns else gets the object from database and
                      puts in the cache.
        :param params: ParamsObject
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data = None
        try:

            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache
            self.pre_get_object(params)
            if isinstance(self, ICachable):
                if self.is_commons_cacheable():
                    cache_key = self.generate_cache_key(self.get_cache_key(), params)
                    data = self.get_object_from_cache(cache_key)
                    if data is None:
                        data = self.get_data_object(params)
                        if data is not None:
                            self.put_object_in_cache(cache_key, data)
                else:
                    data = self.get_data_object(params)
            else:
                data = self.get_data_object(params)

            return self.post_get_object(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get_object(data)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def pre_get_object(self, params):
        """
        :Description: This method should be overridden in the child if child needs to process anything before getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def get_data_object(self, params):
        """
        :Description: This method should be overridden in the child to process the get operation
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def post_get_object(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        return object

    def get_list_object(self, params: ParamsObject):
        """
        :description: This method facilitates callee to get the list of transactional object for any context.
                      If the Object is cacheable then, this method checks the cache first and then
                      id object is in cache it returns else gets the object from database and
                      puts in the cache.
        :param params: ParamsObject
        :return: list of Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data = None
        try:

            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache
            self.pre_get_list_object(params)
            if isinstance(self, ICachable):
                if self.is_commons_cacheable():
                    cache_key = self.generate_cache_key(self.get_cache_key(), params)
                    data = self.get_object_from_cache(cache_key)
                    if data is None:
                        data = self.get_data_list_object(params)
                        if data is not None:
                            self.put_object_in_cache(cache_key, data)
                else:
                    data = self.get_data_list_object(params)
            else:
                data = self.get_data_list_object(params)

            return self.post_get_list_object(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get_list_object(data)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def get_data_list_object(self, params):
        """
        :Description: This method should be overridden in the child to process the get operation
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def pre_get_list_object(self, params):
        """
        :Description: This method should be overridden in the child if child needs to process anything before getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def post_get_list_object(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        return object

    def get_list_object_paginated(self, params: ParamsObject):
        """
        :description: This method facilitates callee to get the list of transactional object for any context                      with pagination.
                      If the Object is cacheable then, this method checks the cache first and then
                      id object is in cache it returns else gets the object from database and
                      puts in the cache.
        :param params: ParamsObject
        :return: list of Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        data = None
        try:

            # Check whether the data in cache
            # If exists in data then get from cache else get from database and put in cache
            self.pre_get_list_object_paginated(params)
            if isinstance(self, ICachable):
                if self.is_commons_cacheable():
                    cache_key = self.generate_cache_key(self.get_cache_key(), params)
                    data = self.get_object_from_cache(cache_key)
                    if data is None:
                        data = self.get_data_list_object_paginated(params)
                        if data is not None:
                            self.put_object_in_cache(cache_key, data)
                else:
                    data = self.get_data_list_object_paginated(params)
            else:
                data = self.get_data_list_object_paginated(params)

            return self.post_get_list_object_paginated(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except CacheException as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", ex.error_message)
            return self.post_get_list_object_paginated(data)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def get_data_list_object_paginated(self, params):
        """
        :Description: This method should be overridden in the child to process the get operation
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def pre_get_list_object_paginated(self, params):
        """
        :Description: This method should be overridden in the child if child needs to process anything before getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        pass

    def post_get_list_object_paginated(self, object):
        """
        :Description: This method should be overridden in the child if child needs to process anything after getting the object
        :param object: ParamsObject
        :return: Actual object (Model)
        """
        return object

    def get_list_object_any(self, sp_name, params: ParamsObject):
        """
        :description: This method facilitates callee to get the list of transactional object for any context                        from particular SP.
        :param sp_name: Procedure name to call
        :param params: params object
        :return: List of Model objects
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            data = self.get_data_list_object_any(sp_name, params)
            return self.post_get_list_object(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def get_data_list_object_any(self, sp_name, params: ParamsObject):
        """
        :Description: This method should be overridden in the child to process the get operation
        :param sp_name: Procedure name to call
        :param params: params object
        :return: List of Model objects
        """
        pass

    def get_list_object_any_paginated(self, sp_name, params: ParamsObject):
        """
        :description: This method facilitates callee to get the list of transactional object for any context                      from particular SP which will always return multiple result set.
        :param sp_name: Procedure name to call
        :param params: params object
        :return: List of Model objects
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            data = self.get_data_list_object_any_paginated(sp_name, params)
            return self.post_get_list_object_paginated(data)
        except DatabaseException as ex:
            # Log the exception if mode is debug
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            self.close_cursor()
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex1:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex1))
            self.rollback()
            raise KaroException(self.general_error_code, str(ex1), None)
        finally:
            self.close_cursor()

    def get_data_list_object_any_paginated(self, sp_name, params):
        """
        :Description: This method should be overridden in the child to process the get operation
        :param sp_name: Procedure name to call
        :param params: params object
        :return: Dictionary contains page and the data(List of Model Object)
        """
        pass
