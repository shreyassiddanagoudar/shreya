"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

from django.core.cache import cache
import redis
import json
from django.conf import settings

from examsystemapp.utils.constants.constants import ErrorCodes
from examsystemapp.utils.exception_handling.exception import CacheException
from examsystemapp.utils.helpers.request_helper import ParamsObject
# from django_redis import get_redis_connection

import pickle


class CacheManager:

    def __init__(self):
        pass

    def get_cache_key(self, object, params: ParamsObject):
        try:
            params_list = params.get_params_list()
            prefix = ""
            if object != "" and object is not None:
                prefix = object
            key = ''.join(str(e) if e is not None else "" for e in params_list)
            return prefix + ':' + key
        except Exception as ex:
            pass

    def put_in_cache(self, key, value):
        return cache.set(key, value, 86400)

    def get_cached(self, key):
        return cache.get(key)

    def invalidate_cache(self, key):
        cache.delete(key)

    def clear_cache(self):
        cache.clear()

    def has_key(self, key):
        if cache.has_key:
            return True
        else:
            return False


class MemcachedCacheManager(CacheManager):

    def __init__(self):
        pass

    def put_in_cache(self, key, value):
        return cache.set(key, value, 86400)

    def get_cached(self, key):
        return cache.get(key)

    def invalidate_cache(self, key):
        cache.delete(key)

    def clear_cache(self):
        cache.clear()

    def has_key(self, key):
        if cache.has_key:
            return True
        else:
            return False


class RedisCacheManager(CacheManager):

    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            if self.connection is None:
                self.connection = redis.Redis(host=settings.CACHE_HOST, port=settings.CACHE_PORT,
                                              password=settings.CACHE_PASS, db=0)
                # self.connection = get_redis_connection('default')
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def get_redis_instance(self):
        try:
            if self.connection is None:
                self.connect()
            return self.connection
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def obj_to_bytes(self, obj):
        try:
            obj_str = json.dumps(obj)
            bytes = ' '.join(format(ord(letter), 'b') for letter in obj_str)
            # bytes = ' '.join(format(ord(letter), 'b') for letter in obj)
            return bytes
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def bytes_to_obj(self, bytes):
        try:
            str_binary = ''.join(chr(int(x, 2)) for x in bytes.split())
            obj = json.loads(str_binary)
            return obj
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def has_key(self, key):
        try:
            if settings.CACHE_ENABLED:
                if self.get_redis_instance().exists(key):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def put_in_cache(self, key, value):
        try:
            if settings.CACHE_ENABLED:
                return self.get_redis_instance().set(key, self.obj_to_bytes(value))
            else:
                return None
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def get_cached(self, key):
        try:
            if settings.CACHE_ENABLED:
                if self.has_key(key):
                    return self.bytes_to_obj(self.get_redis_instance().get(key))
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    # This converts actual object to bytes and stores in cache
    def put_object_in_cache(self, key, object):
        try:
            if settings.CACHE_ENABLED:
                pickled_object = pickle.dumps(object)
                return self.get_redis_instance().set(key, pickled_object)
            else:
                return None
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    # This gets the bytes from the cache and created actual object and returns the object to callee
    def get_object_from_cache(self, key):
        try:
            # if self.has_key(key):
            #     return pickle.loads(self.get_redis_instance().get(key))
            # else:
            #     return None
            if settings.CACHE_ENABLED:
                data_object = self.get_redis_instance().get(key)
                if data_object is not None:
                    data_object = pickle.loads(data_object)

                return data_object
            else:
                return None
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def get_cached_by_ids(self, prefix, keys):
        cached_objects = []
        non_cached_ids = []
        try:
            if settings.CACHE_ENABLED:
                for key in keys:
                    cache_key = prefix + ":" + str(key)
                    if self.has_key(cache_key):
                        cached_objects.append(self.get_cached(cache_key))
                    else:
                        non_cached_ids.append(key)

                return cached_objects, non_cached_ids
            else:
                return cached_objects, non_cached_ids
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    # def get_cached_objects_by_ids(self, prefix, keys):
    #     cached_objects = []
    #     non_cached_ids = []
    #     try:
    #         for key in keys:
    #             cache_key = prefix + ":" + str(key)
    #             data_object = self.get_object_from_cache(cache_key)
    #             if data_object is None:
    #                 non_cached_ids.append(key)
    #             else:
    #                 cached_objects.append(data_object)
    #             # if self.has_key(cache_key):
    #             #     cached_objects.append(self.get_object_from_cache(cache_key))
    #             # else:
    #             #     non_cached_ids.append(key)
    #
    #         return cached_objects, non_cached_ids
    #     except Exception as ex:
    #         raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def get_cached_objects_by_ids(self, prefix, keys):
        cached_objects = []
        non_cached_ids = []
        try:
            if settings.CACHE_ENABLED:
                list_with_prefix = [prefix + ":" + s for s in keys]

                cached_objects = self.get_redis_instance().mget(list_with_prefix)
                cached_objects = [pickle.loads(i) for i in cached_objects if i]

                # exists_keys = [str(each_object.get_id()) for each_object in cached_objects]
                # non_cached_ids = [x for x in keys if x not in exists_keys]

                return cached_objects
            else:
                return cached_objects
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def invalidate_cache(self, key):
        try:
            if settings.CACHE_ENABLED:
                return self.get_redis_instance().delete(key)
            else:
                return True
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def clear_cache(self):
        try:
            if settings.CACHE_ENABLED:
                return self.get_redis_instance().flushall()
            else:
                return True
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def invalidate_cache_by_prefix(self, prefix):
        try:
            if settings.CACHE_ENABLED:
                for key in self.get_redis_instance().scan_iter(prefix + ":*"):
                    self.invalidate_cache(key)
            else:
                pass
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def scan(self, prefix=""):
        try:
            if settings.CACHE_ENABLED:
                list_keys, val = self.get_redis_instance().scan(0, prefix + "*", None)
                return list_keys
            else:
                return list()
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)

    def get_cached_objects_by_keys(self, list_keys):
        try:
            if settings.CACHE_ENABLED:
                cached_objects = self.get_redis_instance().mget(list_keys)
                cached_objects = [pickle.loads(i) for i in cached_objects if i]

                return cached_objects
            else:
                return list()
        except Exception as ex:
            raise CacheException(ErrorCodes.GENERAL_ERROR, str(ex), None)
