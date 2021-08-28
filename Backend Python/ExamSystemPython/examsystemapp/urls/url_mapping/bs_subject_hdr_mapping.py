from examsystemapp.api.bs_subject_hdr import BSSubjectHdr
from examsystemapp.utils.exception_handling.exception import PermissionDeniedException, KaroException
from . import base_url_mapping


def add(request):
    try:
        return BSSubjectHdr(request).add(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def update(request):
    try:
        return BSSubjectHdr(request).update(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def delete(request):
    try:
        return BSSubjectHdr(request).delete(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get(request):
    try:
        return BSSubjectHdr(request).get(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_list(request):
    try:
        return BSSubjectHdr(request).get_list(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_object(request):
    try:
        return BSSubjectHdr(request).get_object(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_list_object(request):
    try:
        return BSSubjectHdr(request).get_list_object(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")


def get_list_object_page(request):
    try:
        return BSSubjectHdr(request).get_list_object_page(request)
    except PermissionDeniedException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 401, ex.error_code)
    except KaroException as ex:
        return base_url_mapping.send_response(None, ex.error_message, 500, ex.error_code)
    except Exception as ex:
        return base_url_mapping.send_response(None, str(ex), 500, "ERROR001")
