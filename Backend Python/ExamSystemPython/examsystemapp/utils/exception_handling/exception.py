"""
Created By : Nikesh
Created On : sss
Reviewed By :
Reviewed On :
Version :
"""


class KaroException(Exception):

    def __init__(self, error_code, error_message, error_object):
        self.error_code = error_code
        self.error_message = error_message
        self.error_object = error_object


class GeneralException(KaroException):

    def __init__(self, error_code, error_message, error_object):
        KaroException.__init__(self, error_code, error_message, error_object)


class DatabaseException(KaroException):

    def __init__(self, error_code, error_message, error_object):
        KaroException.__init__(self, error_code, error_message, error_object)


class PermissionDeniedException(KaroException):

    def __init__(self, error_code, error_message, error_object):
        KaroException.__init__(self, error_code, error_message, error_object)


class CacheException(KaroException):

    def __init__(self, error_code, error_message, error_object):
        KaroException.__init__(self, error_code, error_message, error_object)


class FileUploadException(KaroException):

    def __init__(self, error_code, error_message, error_object):
        KaroException.__init__(self, error_code, error_message, error_object)


class ValidationException(KaroException):

    def __init__(self, error_code, error_message, error_object):
        KaroException.__init__(self, error_code, error_message, error_object)
