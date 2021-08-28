"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from django.db import connections, transaction

from examsystemapp.models.cursor_object import CursorObject
from examsystemapp.utils.exception_handling.exception import DatabaseException, KaroException, FileUploadException
from examsystemapp.utils.helpers.file_helper import FileHelper

from examsystemapp.utils.helpers.logging_helper import LoggingHelper
from examsystem.settings import base
from examsystemapp.utils.constants.constants import ErrorCodes, AppConstants

from django.conf import settings
import random

from examsystemapp.utils.helpers.request_helper import ParamsObject


class BaseRepository:
    """
    This class handles all the database operations
    """

    def __init__(self, ext_params={}, event_type=None):
        self.cursor = None
        self.sp_name = None
        self.params = None
        self.data = []
        self.db_error_code = ErrorCodes.DATABASE_ERROR
        self.general_error_code = ErrorCodes.GENERAL_ERROR
        self.current_db_type = None
        self.read_db_names = None
        self.current_read_db = None
        self.params_list = []
        self.cursor_object = CursorObject()
        self.ext_params = ext_params
        self.event_type = event_type

    def connect(self):
        pass

    def get_cursor(self, db_type='W'):
        if self.cursor is None:
            self.cursor = connections['default'].cursor()
        return self.cursor

    def close_cursor(self):
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None
            self.read_db_names = None

    def data_as_dict(self):
        """
        Loop through the cursor and creates the list of the results
        Returns the list of objects
        """
        self.data = []
        data = self.cursor.fetchall()
        if len(data) > 0:
            column_names_list = [x[0] for x in self.cursor.description]
            self.data = [dict(zip(column_names_list, row)) for row in data]
        self.cursor.nextset()
        return self.data

    def data_as_dict_multiple_rs(self):
        """
        Loop through the cursor and creates the list of the results for the cursor which has multiple result set
        Returns the list of objects with 1,2.. as the key for each result set
        """
        count = 1
        dict_ = {}
        while 1:
            data = self.cursor.fetchall()
            if len(data) > 0:
                column_names_list = [x[0] for x in self.cursor.description]
                data_list = [dict(zip(column_names_list, row)) for row in data]
                if count == 1:
                    dict_["pages"] = data_list[0]
                else:
                    dict_["data"] = data_list
                count = count + 1
                if self.cursor.nextset() is None:
                    break
                if self.cursor.description is None:
                    break
            else:
                break
        if bool(dict_) == False:
            self.data = None
        else:
            self.data = dict_
        return self.data

    def get_data_from_cursor(self):
        """
        :Description: This creates the cursorObject from the cursor and returns to the callee
                      This should be used for the single result set always
        :return: CursorObject
        """
        data = self.cursor.fetchall()
        self.cursor_object.columns = [x[0] for x in self.cursor.description]
        self.cursor_object.data = data
        self.cursor.nextset()
        return self.cursor_object

    def data_as_cursor_dict_multiple_rs(self):
        """
        :Description: This creates the cursorObject from the cursor and returns to the callee
                      This should be used for the multiple result set always
        :return: list of dictionary, which contains the CursorObject
        """
        count = 1
        dict_ = {}
        while 1:
            data = self.cursor.fetchall()
            if len(data) > 0:
                cursor_obj = CursorObject()
                cursor_obj.columns = [x[0] for x in self.cursor.description]
                cursor_obj.data = data
                dict_[str(count)] = cursor_obj
                count = count + 1
                if self.cursor.nextset() is None:
                    break
                if self.cursor.description is None:
                    break
            else:
                break
        self.data.append(dict_)
        return self.data

    def data_as_cursor_list_multiple_rs(self):
        """
        :Description: This creates the cursorObject from the cursor and returns to the callee with list of cursor objects
                      This should be used for the multiple result set always
        :return: list of dictionary, which contains the CursorObject
        """
        cursor_list = []
        while 1:
            data = self.cursor.fetchall()
            if len(data) > 0:
                cursor_obj = CursorObject()
                cursor_obj.columns = [x[0] for x in self.cursor.description]
                cursor_obj.data = data
                cursor_list.append(cursor_obj)
                if self.cursor.nextset() is None:
                    break
                if self.cursor.description is None:
                    break
            else:
                break
        return cursor_list

    def data_as_dict_transactional(self):
        """
        :description: This function should be user for all the transactional procedures i.e add/update/delete
                      This will catch the errors raised by the procedures
                      If there are any errors then it will raise the exception with the error message given                        by the procedure
        :return: data as list
        """
        data = self.cursor.fetchall()
        if len(data) > 0:
            column_names_list = [x[0] for x in self.cursor.description]
            self.data = [dict(zip(column_names_list, row)) for row in data]
        self.cursor.nextset()

        if len(data) > 0:
            dict_ = self.data[0]

            if dict_.get(AppConstants.DB_SUCCESS_KEY) == 1:
                return self.data
            else:
                raise DatabaseException(dict_.get("DB_RESPONSE_CODE"), dict_.get("DB_RESPONSE_MESSAGE"), self.data)
        else:
            raise DatabaseException(ErrorCodes.DATABASE_ERROR, "Did not receive status from database", self.data)

    def add_data(self, object):
        """
        :description: To add the data into the system using the object
        :param object: Actual Object (Model)
        :return: Actual Added object (Model)
        """
        try:
            self.pre_add(object)
            self.get_cursor(db_type="W").callproc(self.sp_name, self.params_list)
            returned_dict = self.data_as_dict_transactional()
            return self.post_add(object, returned_dict[0])
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, ex.error_object)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_add(self, object):
        pass

    def post_add(self, object, returned_dict):
        return object.set_id(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

    def update_data(self, object):
        try:
            self.pre_update(object)
            self.get_cursor(db_type="W").callproc(self.sp_name, self.params_list)
            returned_dict = self.data_as_dict_transactional()
            return self.post_update(object, returned_dict[0])
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, ex.error_object)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_update(self, object):
        pass

    def post_update(self, object, returned_dict):
        return object

    def delete_data(self, object):
        try:
            self.pre_delete(object)
            self.get_cursor(db_type="W").callproc(self.sp_name, self.params_list)
            returned_data = self.data_as_dict_transactional()
            return self.post_delete(object, returned_data[0])
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, ex.error_object)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_delete(self, object):
        pass

    def post_delete(self, object, returned_data):
        pass

    def get_data(self, params):
        try:
            self.pre_get(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get(cursor_object)
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_get(self, params):
        pass

    def post_get(self, cursor_object):
        pass

    def get_data_object(self, params):
        try:
            self.pre_get_object(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get_object(cursor_object)
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_get_object(self, params):
        pass

    def post_get_object(self, cursor_object):
        pass

    def get_data_list(self, params):
        try:
            self.pre_get_list(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get_list(cursor_object)
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_get_list(self, params):
        pass

    def post_get_list(self, cursor_object):
        pass

    def get_data_list_object(self, params):
        try:
            self.pre_get_list_object(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get_list_object(cursor_object)
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_get_list_object(self, params):
        pass

    def post_get_list_object(self, cursor_object):
        pass

    def get_data_list_object_paginated(self, params):
        try:
            self.pre_get_data_list_object_paginated(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            list_cursor_object = self.data_as_cursor_list_multiple_rs()
            return self.post_get_data_list_object_paginated(list_cursor_object)
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()

    def pre_get_data_list_object_paginated(self, params):
        pass

    def post_get_data_list_object_paginated(self, list_cursor_object):
        pass

    def execute_raw_sql(self, sql_query):
        try:
            self.get_cursor(db_type="W").excecute(sql_query)
            self.data_as_dict()
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        return self.data

    def execute_raw_sql_multiple(self, sql_query):
        try:
            self.get_cursor(db_type="W").excecute(sql_query)
            self.data_as_dict_multiple_rs()
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        return self.data

    def call_direct(self, sp_name, params, db_type='R'):
        try:
            self.get_cursor(db_type).callproc(sp_name, params)
            self.data_as_dict()
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        return self.data

    def call_direct_multiple(self, sp_name, params, db_type='R'):
        try:
            self.get_cursor(db_type).callproc(sp_name, params)
            self.data_as_dict_multiple_rs()
        except Exception as ex:
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        return self.data

    def get_direct(self, sp_name, params):
        return self.call_direct(sp_name, params, db_type='R')

    def get_direct_multiple(self, sp_name, params):
        return self.call_direct_multiple(sp_name, params, db_type='R')

    def build_dict_for_cursor(self, cursor_object: CursorObject):
        column_names_list = cursor_object.get_columns()
        data = [dict(zip(column_names_list, row)) for row in cursor_object.get_data()]
        return data[0]

    def build_paginated_result(self, pagination_cursor_object, model_object):
        result_dict = {}
        result_dict["pages"] = self.build_dict_for_cursor(pagination_cursor_object)
        result_dict["data"] = model_object
        return result_dict

    def call_direct_with_transaction(self, sp_name, params, db_type='W'):
        """
        :description: This function facilitates to call the sp directly  (For add/update/delete)
                      Function requires sp_name as string and params as list
                      It does not provide the transaction and it does not closes the cursor
                      Returns the data object to the data layer
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :param db_type: Type of database (Read or write)
        :return: List of dictionary (Whatever comes from the database directly)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, sp_name, params)
        try:
            # transaction.set_autocommit(autocommit=False)
            self.get_cursor(db_type).callproc(sp_name, params)
            self.data_as_dict_transactional()
            # transaction.commit()
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, ex.error_object)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", self.data)
        return self.data