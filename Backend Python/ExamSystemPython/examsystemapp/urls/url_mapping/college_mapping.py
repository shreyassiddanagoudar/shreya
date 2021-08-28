from examsystemapp.api.college import College
from examsystemapp.utils.exception_handling.exception import PermissionDeniedException, KaroException
from . import base_url_mapping


def add(request):
    try:
        return College(request).add(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def update(request):
    try:
        return College(request).update(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def delete(request):
    try:
        return College(request).delete(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get(request):
    try:
        return College(request).get(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_list(request):
    try:
        return College(request).get_list(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_object(request):
    try:
        return College(request).get_object(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_list_object(request):
    try:
        return College(request).get_list_object(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_list_object_page(request):
    try:
        return College(request).get_list_object_page(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")
