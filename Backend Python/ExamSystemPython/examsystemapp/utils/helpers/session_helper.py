"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import base64
import hashlib
import pickle

from django.conf import settings
import jwt
from cryptography.fernet import Fernet


class SessionHelper:

    def __init__(self):
        self.default_key = "USER_DATA"
        self.expiry_time = 300

        self.user_id_key = "User_ID"
        self.entity_id_key = "Entity_ID"

    def has_key(self, request, key=None):
        if key is None:
            key = self.default_key

        if key in request.session:
            return True
        else:
            return False

    def get_session(self, request, key=None):
        if key is None:
            key = self.default_key

        if self.has_key(key, request):
            return request.session[key]
        else:
            return None

    def set_session(self, request, data, key=None):
        if key is None:
            key = self.default_key
        if self.has_key(request, key):
            pass
        else:
            request.session[key] = data

    def get_session_user_id(self, request):
        if self.has_key(request):
            data: dict = self.get_session(request)[0]
            return data[self.user_id_key]
        else:
            return None

    def get_session_entity_id(self, request):
        if self.has_key(request):
            data: dict = self.get_session(request)[0]
            return data[self.entity_id_key]
        else:
            return None

    def get_user_data_by_key(self, request, key):
        if self.has_key(request):
            data: dict = self.get_session(request)[0]
            return data[key]
        else:
            return None


class JWTManager:

    @staticmethod
    def generate_token(payload: dict):
        return jwt.encode(payload, settings.TOKEN_SECRETE, algorithm='HS256').decode("utf-8")

    @staticmethod
    def decode_token(token):
        payload = jwt.decode(token, settings.TOKEN_SECRETE, algorithms=['HS256'])
        return payload

    @staticmethod
    def get_payload_value_by_key(payload, key):
        return payload.get(key, None)

    @staticmethod
    def get_token_value_by_key(token, key):
        payload = JWTManager.decode_token(token)
        return payload.get(key, None)

    @staticmethod
    def get_checksum(data):
        return hashlib.md5(pickle.dumps(data)).hexdigest()


class BaseEncryption:
    def __init__(self):
        pass

    def encrypt(self, val):
        pass

    def decrypt(self, encrypted_val):
        pass


class Base64Encryption(BaseEncryption):

    def __init__(self):
        BaseEncryption.__init__(self)

    def encrypt(self, val):
        return base64.encode(val)

    def decrypt(self, encrypted_val):
        return base64.decode(encrypted_val)


class CryptographyEncryption(BaseEncryption):

    def __init__(self):
        BaseEncryption.__init__(self)

    def encrypt(self, val):
        key = bytes(settings.APP_SECRETE)
        f = Fernet(key)
        return f.encrypt(bytes(val))

    def decrypt(self, encrypted_val):
        key = bytes(settings.APP_SECRETE)
        f = Fernet(key)
        return f.decrypt(bytes(encrypted_val))
