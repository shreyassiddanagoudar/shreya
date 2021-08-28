from .base import *

DEBUG = True

APP_SECRETE = "da418aa55f9458a62f523a3aaf5ec6083bb89b0f"
TOKEN_SECRETE = "K@r0Sambhav"

CACHE_HOST = "dev.sustainablecontext.com"
CACHE_PORT = 6379
CACHE_PASS = "K@r0Sambhav2018"

CACHE_ENABLED = True

ALLOWED_HOSTS = ['*']

ASSET_SERVER_BASE_URL = "http://127.0.0.1:8001/"
ASSET_SERVER_UPLOAD_URL = ASSET_SERVER_BASE_URL + "api/assets/file-draft/add"
ASSET_SERVER_COMMIT_URL = ASSET_SERVER_BASE_URL + "api/assets/file/add"
ASSET_SERVER_COMMIT_MULTIPLE_URL = ASSET_SERVER_BASE_URL + "api/assets/file/add-multiple"
ASSET_SERVER_DOWNLOAD_URL = ASSET_SERVER_BASE_URL + "api/assets/asset/download"
ASSET_SERVER_VIEW_URL = ASSET_SERVER_BASE_URL + "api/assets/asset/view"
ASSET_SERVER_DELETE_URL = ASSET_SERVER_BASE_URL + "api/assets/asset-ops/delete"
ASSET_SERVER_GET_FILES_URL = ASSET_SERVER_BASE_URL + "api/assets/file/get-object"
ASSET_SERVER_GET_OBJECT_LIST_URL = ASSET_SERVER_BASE_URL + "api/assets/object/get-list-object"
ASSET_SERVER_GET_DOCUMENT_LIST_URL = ASSET_SERVER_BASE_URL + "api/assets/document/get-list-object"
ASSET_SERVER_GET_OBJECT_DOCUMENT_LIST_URL = ASSET_SERVER_BASE_URL + "api/assets/object-document/get-list"
ASSET_SERVER_GET_FILES_MULTIPLE_URL = ASSET_SERVER_BASE_URL + "api/assets/file/get-list-object"
ASSET_SERVER_GET_OBJECT_DOCUMENT_LIST_MULTIPLE_URL = ASSET_SERVER_BASE_URL + "api/assets/object-document/get-list-object-multiple"
ASSET_SERVER_GET_FILES_MULTIPLE_TRANS_URL = ASSET_SERVER_BASE_URL + "api/assets/file/get-list-object-multi-trans"
ASSET_SERVER_GET_DOCUMENT_UPLOADED_URL = ASSET_SERVER_BASE_URL + "api/assets/file/get-uploaded-number"
ASSET_SERVER_GET_OBJECT_DOCUMENT_ACCESS_URL = ASSET_SERVER_BASE_URL + "api/assets/object-document-access/get-list-object"
ASSET_SERVER_GET_ALL_FILES_URL = ASSET_SERVER_BASE_URL + "api/assets/file/get-all-files"
ASSET_SERVER_CHANGE_FILE_NAME_URL = ASSET_SERVER_BASE_URL + "api/assets/file/change-file-name"
ASSET_SERVER_MOVE_FILE_URL = ASSET_SERVER_BASE_URL + "api/assets/file/move-file"

WKHTMLTOPDF_PATH = os.path.join("C:/", "Program Files", "wkhtmltopdf", "bin", "wkhtmltopdf.exe")

MASTER_BASE_URL = "http://localhost:8002"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'examsystem',
        'USER': 'itfyme',
        'PASSWORD': 'itfyme',
        'HOST': '13.71.16.66',
        'PORT': '3306',
    }
}
