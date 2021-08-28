"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import json

import requests
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpRequest

from examsystemapp.utils.constants.constants import ErrorCodes
from examsystemapp.utils.exception_handling.exception import FileUploadException


def convert_to_dict(obj):
    return obj.__dict__


class FileHelper:

    def __init__(self):
        pass

    def upload_file(self, request: HttpRequest, transaction_type, object, is_token_needed=True):
        files = dict()
        data = dict()
        headers = dict()
        try:
            if len(request.FILES) > 0:
                # for key, file in request.FILES.items():
                #     file: InMemoryUploadedFile = file
                #     files[key] = file

                file_keys = request.FILES.keys()
                cnt = 0
                for key in file_keys:
                    file_data = request.FILES.getlist(key)
                    for each_file in file_data:
                        file: InMemoryUploadedFile = each_file
                        files["file_" + str(cnt)] = file
                        cnt = cnt + 1

                data["transaction_type"] = transaction_type
                data["object"] = object

                if is_token_needed:
                    headers["TOKEN"] = settings.APP_SECRETE

                response = requests.post(settings.ASSET_SERVER_UPLOAD_URL, files=files, data=data, headers=headers)
                json_data = response.json()
                return json_data.get("response_object")
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # Final
    def upload(self, request: HttpRequest):
        files = dict()
        headers = dict()
        try:
            if len(request.FILES) > 0:
                file_keys = request.FILES.keys()
                cnt = 0
                for key in file_keys:
                    file_data = request.FILES.getlist(key)
                    for each_file in file_data:
                        file: InMemoryUploadedFile = each_file
                        files["file_" + str(cnt)] = file
                        cnt = cnt + 1

                data = dict()
                data["object_type"] = request.POST.get("object_type")
                data["document_type"] = request.POST.get("document_type")
                data["app_id"] = "Karo-app"
                data["transaction_id"] = request.POST.get("transaction_id")
                data["created_by"] = request.POST.get("created_by")

                post_data = {"file_draft_json": json.dumps(data)}

                response = requests.post(settings.ASSET_SERVER_UPLOAD_URL, files=files, data=post_data, headers=headers)
                json_data = response.json()
                return json_data
                # return json_data.get("response_object")
            else:
                raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, "There are no files in the request", None)
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # def commit(self, draft_object, transaction_id, transaction_type, object, context, is_token_needed=True):
    #     data = dict()
    #     headers = dict()
    #     try:
    #         if draft_object != "" and draft_object is not None:
    #             data["transaction_id"] = transaction_id
    #             data["context"] = context
    #             data["transaction_type"] = transaction_type
    #             data["object"] = object
    #             data["draft_object"] = json.dumps(draft_object)
    #
    #             if is_token_needed:
    #                 headers["TOKEN"] = settings.APP_SECRETE
    #
    #             response = requests.post(settings.ASSET_SERVER_COMMIT_URL, data=data, headers=headers)
    #             json_data = response.json()
    #             return json_data.get("response_object")
    #     except Exception as ex:
    #         raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # Final
    def commit(self, draft_object, transaction_id, created_by, data_object):
        data = dict()
        headers = dict()
        try:
            if draft_object != "" and draft_object is not None:
                data["app_id"] = "Karo-app"
                data["created_by"] = created_by
                data["transaction_id"] = transaction_id
                data["draft"] = draft_object
                data["data_object"] = json.dumps(data_object, default=convert_to_dict, indent=2, cls=DjangoJSONEncoder)

                post_data = {"file_header_json": json.dumps(data)}

                response = requests.post(settings.ASSET_SERVER_COMMIT_URL, data=post_data, headers=headers)
                json_data = response.json()
                return json_data
                # return json_data.get("response_object")
            else:
                raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, "Draft object is mandatory", None)
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # Final
    def commit_all(self, file_detail_objects, created_by):
        data = dict()
        headers = dict()
        try:
            if file_detail_objects != "" and file_detail_objects is not None:
                data["app_id"] = "Karo-app"
                data["created_by"] = created_by
                data["files"] = file_detail_objects

                post_data = {"file_json": json.dumps(data)}

                response = requests.post(settings.ASSET_SERVER_COMMIT_MULTIPLE_URL, data=post_data, headers=headers)
                json_data = response.json()
                return json_data
                # return json_data.get("response_object")
            else:
                raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, "Draft object is mandatory", None)
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # Final
    def delete(self, file_object, delete_by):
        # data = dict()
        headers = dict()
        try:
            if file_object != "" and file_object is not None:
                post_data = {
                    "file_object": file_object,
                    "delete_by": delete_by
                }
                response = requests.post(settings.ASSET_SERVER_DELETE_URL, data=post_data, headers=headers)
                json_data = response.json()
                return json_data
                # return json_data.get("response_object")
            else:
                raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, "File object is mandatory", None)
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def delete_file(self, file_object, is_token_needed=True):
        data = dict()
        headers = dict()
        try:
            if file_object != "" and file_object is not None:
                data["file_object"] = file_object

                if is_token_needed:
                    headers["TOKEN"] = settings.APP_SECRETE

                response = requests.post(settings.ASSET_SERVER_DELETE_URL, data=data, headers=headers)
                json_data = response.json()
                return json_data
                # return json_data.get("response_object")
            else:
                raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, "File object is mandatory", None)
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # def get_files(self, transaction_id, transaction_type, object, is_token_needed=True):
    #     headers = dict()
    #     get_files_url = settings.ASSET_SERVER_GET_FILES_URL
    #     get_files_url = get_files_url + "?transaction_id=" + str(transaction_id) + "&transaction_type=" + str(
    #         transaction_type) + "&object=" + object
    #     try:
    #         if is_token_needed:
    #             headers["TOKEN"] = settings.APP_SECRETE
    #
    #         response = requests.get(get_files_url, headers=headers)
    #         json_data = response.json()
    #         return json_data.get("response_object")
    #     except Exception as ex:
    #         raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    # Final
    def get_files(self, transaction_id, object_type, document_type, object_id, document_id):
        headers = dict()
        get_files_url = settings.ASSET_SERVER_GET_FILES_URL
        get_files_url = get_files_url + "?app_id=Karo-app&transaction_id=" + str(
            transaction_id) + "&object_type=" + str(object_type) + "&document_type=" + str(
            document_type) + "&object_id=" + str(
            object_id) + "&document_id=" + str(document_id)
        try:
            response = requests.get(get_files_url, headers=headers)
            json_data = response.json()
            return json_data
            # return json_data.get("response_object")
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_files_multiple(self, transaction_id, object_type, document_type, object_id, document_id):
        headers = dict()
        get_files_url = settings.ASSET_SERVER_GET_FILES_MULTIPLE_URL
        get_files_url = get_files_url + "?app_id=Karo-app&transaction_id=" + str(
            transaction_id) + "&object_type=" + str(object_type) + "&document_type=" + str(
            document_type) + "&object_id=" + str(
            object_id) + "&document_id=" + str(document_id)
        try:
            response = requests.get(get_files_url, headers=headers)
            json_data = response.json()
            return json_data
            # return json_data.get("response_object")
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_files_multiple_transaction(self, transaction_ids, object_type):
        headers = dict()
        get_files_url = settings.ASSET_SERVER_GET_FILES_MULTIPLE_TRANS_URL
        get_files_url = get_files_url + "?app_id=Karo-app&transaction_ids=" + str(
            transaction_ids) + "&object_type=" + str(object_type)
        try:
            response = requests.get(get_files_url, headers=headers)
            json_data = response.json()
            return json_data
            # return json_data.get("response_object")
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_object_list(self):
        headers = dict()
        get_object_list_url = settings.ASSET_SERVER_GET_OBJECT_LIST_URL + "?app_id=Karo-app"
        try:
            response = requests.get(get_object_list_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_document_list(self):
        headers = dict()
        get_document_list_url = settings.ASSET_SERVER_GET_DOCUMENT_LIST_URL + "?app_id=Karo-app"
        try:
            response = requests.get(get_document_list_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_document_list_by_id(self, ids=''):
        headers = dict()
        get_document_list_url = settings.ASSET_SERVER_GET_DOCUMENT_LIST_BY_IDS_URL + "?ids="+str(ids)+""
        try:
            response = requests.get(get_document_list_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_document_list_by_type(self, types=''):
        headers = dict()
        get_document_list_url = settings.ASSET_SERVER_GET_DOCUMENT_LIST_BY_TYPE_URL + "?doc_types="+str(types)+""
        try:
            response = requests.get(get_document_list_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_object_document_list(self):
        headers = dict()
        get_object_document_list_url = settings.ASSET_SERVER_GET_OBJECT_DOCUMENT_LIST_URL + "?ids="
        try:
            response = requests.get(get_object_document_list_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_object_document_list_multiple(self, object_type=''):
        headers = dict()
        get_object_document_list_url = settings.ASSET_SERVER_GET_OBJECT_DOCUMENT_LIST_MULTIPLE_URL + "?object_type=" + object_type
        try:
            response = requests.get(get_object_document_list_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_object_document_access(self, object_document_id, role_ids):
        headers = dict()
        role_ids_str = ''
        if object_document_id is None or object_document_id == 0:
            object_document_id = ''

        if len(role_ids) <= 0:
            return None
        else:
            role_ids_str = ','.join([str(i) for i in role_ids])

        get_object_document_access_url = settings.ASSET_SERVER_GET_OBJECT_DOCUMENT_ACCESS_URL + "?object_document_id=" + object_document_id + "&role_ids=" + role_ids_str
        try:
            response = requests.get(get_object_document_access_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_uploaded_document_number(self, transaction_id, object_type):
        headers = dict()

        get_files_url = settings.ASSET_SERVER_GET_DOCUMENT_UPLOADED_URL
        get_files_url = get_files_url + '?transaction_id' + str(transaction_id) + "&object_type=" + str(object_type)
        try:
            response = requests.get(get_files_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def get_all_files(self, from_date, to_date, page_num, page_size):
        headers = dict()

        get_files_url = settings.ASSET_SERVER_GET_ALL_FILES_URL
        get_files_url = get_files_url + '?from_date' + str(from_date) + "&to_date=" + str(to_date) + "&page_num=" + str(
            page_num) + "&page_size=" + str(page_size)
        try:
            response = requests.get(get_files_url, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def change_file_name(self, user_id, transaction_id, object_type, document_type, file_name, file_original_name):
        data = dict()
        headers = dict()
        try:
            data["app_id"] = "Karo-app"
            data["user_id"] = user_id
            data["transaction_id"] = transaction_id
            data["object_type"] = object_type
            data["document_type"] = document_type
            data["file_name"] = file_name
            data["file_original_name"] = file_original_name

            post_data = {"file_json": json.dumps(data)}

            response = requests.post(settings.ASSET_SERVER_CHANGE_FILE_NAME_URL, data=post_data, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)

    def move_file(self, user_id, transaction_id, object_type, old_document_type, document_type, file_name):
        data = dict()
        headers = dict()
        try:
            data["app_id"] = "Karo-app"
            data["user_id"] = user_id
            data["transaction_id"] = transaction_id
            data["object_type"] = object_type
            data["old_document_type"] = old_document_type
            data["document_type"] = document_type
            data["file_name"] = file_name

            post_data = {"file_json": json.dumps(data)}

            response = requests.post(settings.ASSET_SERVER_MOVE_FILE_URL, data=post_data, headers=headers)
            json_data = response.json()
            return json_data
        except Exception as ex:
            raise FileUploadException(ErrorCodes.FILE_UPLOAD_ERROR, str(ex), None)
