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
        """
        :description: Get cursor based on the database type
        :param db_type: W - To get the connection to Write database
                        R - To get the connection to Read database
        :return: the cursor for the connected database
        """
        if self.current_db_type is None:
            self.current_db_type = db_type
        else:
            if self.current_db_type != db_type:
                if self.cursor is not None:
                    self.cursor.close()
                self.cursor = None
                self.current_db_type = db_type

        if db_type == 'W':
            if self.cursor is None:
                self.cursor = connections['default'].cursor()
            return self.cursor
        else:
            """
            Randomly select the Read databases
            If connection to a database fails then try connecting to other read databases
            If all the connection fails then read from Write database itself
            """

            if not transaction.get_autocommit():
                self.cursor = connections['default'].cursor()

            if self.cursor is None:

                if self.read_db_names is None:
                    database_dict: dict = settings.DATABASES
                    database_conf: dict = dict()
                    for key in database_dict:
                        database_conf[key] = database_dict.get(key)
                    database_conf.pop('default', None)
                    self.read_db_names = list(database_conf.keys())

                if len(self.read_db_names) <= 0:
                    self.cursor = connections['default'].cursor()
                else:
                    try:
                        self.current_read_db = random.choice(self.read_db_names)
                        self.cursor = connections[self.current_read_db].cursor()
                    except Exception as e:
                        self.cursor = None
                        self.read_db_names.remove(self.current_read_db)
                        self.get_cursor(db_type="R")
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
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            self.pre_add(object)
            self.get_cursor(db_type="W").callproc(self.sp_name, self.params_list)
            returned_dict = self.data_as_dict_transactional()
            return self.post_add(object, returned_dict[0])
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

    def pre_add(self, object):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: Actual Object (Model)
        :return: Void
        """
        pass

    def post_add(self, object, returned_dict):
        """
        :description: should be overridden the to do create actual object after adding
        :param object: Actual Object (Model)
        :param returned_dict: dictionary
        :return: Actual object (Model)
        """
        return object.set_id(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

    def update_data(self, object):
        """
        :description: To update the data in the system using the object
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            self.pre_update(object)
            self.get_cursor(db_type="W").callproc(self.sp_name, self.params_list)
            returned_dict = self.data_as_dict_transactional()
            return self.post_update(object, returned_dict[0])
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

    def pre_update(self, object):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: Actual Object (Model)
        :return: Void
        """
        pass

    def post_update(self, object, returned_dict):
        """
        :description: should be overridden the to do create actual object after updating
        :param object: Actual Object (Model)
        :param returned_dict: dictionary
        :return: Actual object (Model)
        """
        return object

    def delete_data(self, object):
        """
        :description: To delete the data from the system using the object
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", object)
        try:
            self.pre_delete(object)
            self.get_cursor(db_type="W").callproc(self.sp_name, self.params_list)
            returned_data = self.data_as_dict_transactional()
            return self.post_delete(object, returned_data[0])
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

    def pre_delete(self, object):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: Actual Object (Model)
        :return: Void
        """
        pass

    def post_delete(self, object, returned_data):
        """
        :description: should be overridden the to do create actual object after deleting
        :param object: Actual Object (Model)
        :param returned_dict: dictionary
        :return: Actual object (Model)
        """
        pass

    def get_data(self, params):
        """
        :description: To get the data from the system using id
        :param params: Actual Object (Model)
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.pre_get(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get(cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def pre_get(self, params):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: ParamsObject
        :return: Void
        """
        pass

    def post_get(self, cursor_object):
        """
        :description: should be overridden the to do create actual object after updating
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        pass

    def get_data_object(self, params):
        """
        :description: To get the data from the system using any context for the transactional object
        :param params: Actual Object (Model)
        :return: Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.pre_get_object(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get_object(cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def pre_get_object(self, params):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: ParamsObject
        :return: Void
        """
        pass

    def post_get_object(self, cursor_object):
        """
        :description: should be overridden the to do create actual object after updating
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        pass

    def get_data_list(self, params):
        """
        :description: To get the list of data from the system using ids
        :param object: ParamsObject
        :return: List of Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.pre_get_list(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get_list(cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def pre_get_list(self, params):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: ParamsObject
        :return: Void
        """
        pass

    def post_get_list(self, cursor_object):
        """
        :description: should be overridden the to do create actual object after updating
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        pass

    def get_data_list_object(self, params):
        """
        :description: To get the list of data from the system for any context for the transactional object
        :param object: ParamsObject
        :return: List of Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.pre_get_list_object(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            cursor_object = self.get_data_from_cursor()
            return self.post_get_list_object(cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def pre_get_list_object(self, params):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: ParamsObject
        :return: Void
        """
        pass

    def post_get_list_object(self, cursor_object):
        """
        :description: should be overridden the to do create actual object after updating
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        pass

    def get_data_list_object_paginated(self, params):
        """
        :description: To get the list of data from the system for any context for the transactional object with pagination
        :param object: ParamsObject
        :return: List of Actual object (Model)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.pre_get_data_list_object_paginated(params)
            self.get_cursor(db_type="R").callproc(self.sp_name, self.params_list)
            list_cursor_object = self.data_as_cursor_list_multiple_rs()
            return self.post_get_data_list_object_paginated(list_cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def pre_get_data_list_object_paginated(self, params):
        """
        :description: should be overridden the to add the sp_name and the parameters
        :param object: ParamsObject
        :return: Void
        """
        pass

    def post_get_data_list_object_paginated(self, list_cursor_object):
        """
        :description: should be overridden the to do create actual object after updating
        :param object: Actual Object (Model)
        :return: Actual object (Model)
        """
        pass

    def get_data_list_object_any(self, sp_name, params: ParamsObject):
        """
        :description: This method allows user to get the data list object for any procedure which always                            returns the model object
        :param sp_name: Procedure name to call
        :param params: list of parameters
        :return: List of model object
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.get_cursor(db_type="R").callproc(sp_name, params.get_params_list())
            cursor_object = self.get_data_from_cursor()
            return self.post_get_list_object(cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def get_data_list_object_any_paginated(self, sp_name, params: ParamsObject):
        """
        :description: This method allows user to get the data list object for any procedure which always                            returns the model object with pagination
        :param sp_name: Procedure name to call
        :param params: list of parameters
        :return: List of model object
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", params)
        try:
            self.get_cursor(db_type="R").callproc(sp_name, params.get_params_list())
            list_cursor_object = self.data_as_cursor_list_multiple_rs()
            return self.post_get_data_list_object_paginated(list_cursor_object)
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
            if base.DEBUG_ENABLED:
                LoggingHelper().log_debug(self.__class__, "", self.data)

    def execute_raw_sql(self, sql_query):
        """
        :description: This executes the raw sql and returns the data object to the business layer
                      This should be used only for single result set
        :param sql_query: raw sql query
        :return: list of dictionary (Whatever coming from the database as is)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", sql_query)
        try:
            self.get_cursor(db_type="W").excecute(sql_query)
            self.data_as_dict()
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", self.data)
        return self.data

    def execute_raw_sql_multiple(self, sql_query):
        """
        :description: This executes the raw sql and returns the data object to the business layer
                      This should be used only for multiple result set
        :param sql_query: raw sql query
        :return: list of dictionary (Whatever coming from the database as is)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", sql_query)
        try:
            self.get_cursor(db_type="W").excecute(sql_query)
            self.data_as_dict_multiple_rs()
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", self.data)
        return self.data

    def call_direct(self, sp_name, params, db_type='R'):
        """
        :description: This function facilitates to call the sp directly
                      Function requires sp_name as string and params as list
                      It does not provide the transaction
                      THis should be used only for single result set
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :param db_type: Type of database (Read or write)
        :return: List of dictionary (Whatever coming from the database directly)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, sp_name, params)
        try:
            self.get_cursor(db_type).callproc(sp_name, params)
            self.data_as_dict()
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", self.data)
        return self.data

    def call_direct_multiple(self, sp_name, params, db_type='R'):
        """
        :description: This function facilitates to call the sp directly
                      Function requires sp_name as string and params as list
                      It does not provide the transaction
                      THis should be used only for multiple result set
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :param db_type: Type of database (Read or write)
        :return: List of dictionary (Whatever coming from the database directly)
        """
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, sp_name, params)
            LoggingHelper().log_debug(self.__class__, sp_name, params)
        try:
            self.get_cursor(db_type).callproc(sp_name, params)
            self.data_as_dict_multiple_rs()
        except Exception as ex:
            if base.DEBUG_ENABLED:
                LoggingHelper().log_error(self.__class__, "", str(ex))
            if isinstance(ex, DatabaseException) or isinstance(ex, KaroException):
                raise DatabaseException(self.db_error_code, ex.error_message, self.data)
            else:
                raise DatabaseException(self.db_error_code, str(ex), self.data)
        finally:
            self.close_cursor()
        if base.DEBUG_ENABLED:
            LoggingHelper().log_debug(self.__class__, "", self.data)
        return self.data

    def call_direct_without_commit(self, sp_name, params, db_type='R'):
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
            self.get_cursor(db_type).callproc(sp_name, params)
            self.data_as_dict_transactional()
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

    def add_direct(self, sp_name, params):
        """
        :description: Call the call_direct_with_transaction to facilitate the direct addition using sp_name                        and params
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :return: List of dictionary (Whatever comes from the database directly)
        """
        return self.call_direct_with_transaction(sp_name, params, db_type='W')

    def update_direct(self, sp_name, params):
        """
        :description: Call the call_direct_with_transaction to facilitate the direct updation using sp_name                        and params
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :return: List of dictionary (Whatever comes from the database directly)
        """
        return self.call_direct_with_transaction(sp_name, params, db_type='W')

    def delete_direct(self, sp_name, params):
        """
        :description: Call the call_direct_with_transaction to facilitate the direct deletion using sp_name                        and params
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :return: List of dictionary (Whatever comes from the database directly)
        """
        return self.call_direct_with_transaction(sp_name, params, db_type='W')

    def get_direct(self, sp_name, params):
        """
        :description:  Call the call_direct to facilitate the direct get using sp_name and params
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :return: List of dictionary (Whatever comes from the database directly)
        """
        return self.call_direct(sp_name, params, db_type='R')

    def get_direct_multiple(self, sp_name, params):
        """
        :description: Call the call_direct_multiple to facilitate the direct get which returns the multiple
        :param sp_name: Procedure name to call
        :param params: list of parameters to call the sp
        :return: List of dictionary (Whatever comes from the database directly)
        """
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

    def file_commit(self, files, transaction_id, created_by, data_object):
        """
        :param files: List of file object (Draft object), which was sent by the Asset server while uploading
        :param transaction_id: Object Id
        :param created_by: Type of object
        :param data_object: On what context file is being uploaded into the system
        :return: List of uploaded files
        """
        try:
            return FileHelper().commit(files, transaction_id, created_by,
                                       data_object)
        except FileUploadException as ex:
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex:
            raise KaroException(self.general_error_code, str(ex), None)

    def file_commit_all(self, files, transaction_id, created_by, data_object):
        """
        :param files: List of file object (Draft object), which was sent by the Asset server while uploading
        :param transaction_id: Object Id\
        :param created_by: Type of object
        :param data_object: On what context file is being uploaded into the system
        :return: List of uploaded files
        """
        try:

            file_list = list()
            file_dict = dict()
            file_dict['transaction_id'] = transaction_id
            file_dict['data_object'] = data_object
            file_dict['files'] = files
            file_list.append(file_dict)
            return FileHelper().commit_all(file_list, created_by)
        except FileUploadException as ex:
            raise KaroException(ex.error_code, ex.error_message, ex.error_object)
        except Exception as ex:
            raise KaroException(self.general_error_code, str(ex), None)
