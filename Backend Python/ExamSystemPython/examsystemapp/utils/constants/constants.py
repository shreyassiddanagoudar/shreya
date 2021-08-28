"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

from enum import Enum


class HttpMethodType(Enum):
    post = 'POST'
    get = 'GET'
    put = 'PUT'
    delete = 'DELETE'


class ErrorCodes:
    GENERAL_ERROR = "ERROR001"
    DATABASE_ERROR = "ERROR002"
    PERMISSION_DENIED = "ERROR003"
    FILE_UPLOAD_ERROR = "ERROR004"
    VALIDATION_ERROR = "ERROR005"
    TOKEN_EXPIRED = "ERROR006"
    MALFUNCTIONED_TOKEN = "ERROR007"
    EXCELERROR = "ERROR008"


class DataTypes:
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    DATE = "date"
    DATETIME = "datetime"


class AppConstants:
    DB_SUCCESS_KEY = "IS_SUCCESS"
    DB_TRANSACTION_ID_KEY = "TRANSACTION_ID"
    DB_RESPONSE_MESSAGE_KEY = "DB_RESPONSE_MESSAGE"
    PAGE_NUMBER_KEY = "page_num"
    PAGE_SIZE_KEY = "page_size"
    ENTITY_ID_KEY = "entity_id"
    USER_ID_KEY = "user_id"
    STATUS_KEY = "status"
    FROM_DATE_KEY = "from_date"
    TO_DATE_KEY = "to_date"
    HIERARCHY_TYPE = "hierarchy_type"
    TOKEN_EXPIRY_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class ObjectTypes:
    SELLER_INVOICE = "SELLERINV"
    KARO_INVOICE = "KAROINV"
    BC_SELLER_INVOICE = "BCSI"
    BC_KARO_INVOICE = "BCKI"
