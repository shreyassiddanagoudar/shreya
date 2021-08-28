"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.city import CityModel
from examsystemapp.repository.base_repository import BaseRepository
from examsystemapp.utils.constants.constants import AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, StringHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class CityRepo(BaseRepository):

    def __init__(self, ext_params={}):
        BaseRepository.__init__(self, ext_params)

    def pre_add(self, object: CityModel):
        self.sp_name = "sCityAdd"
        list_params = [object.stateid,object.name,object.code]
        self.params_list = list_params

    def post_add(self, object, returned_dict):
        city_model: CityModel = object
        city_model.cityid = int(returned_dict.get(AppConstants.DB_TRANSACTION_ID_KEY))

        return city_model

    def pre_update(self, object: CityModel):
        self.sp_name = "sCityUpdate"
        list_params = [object.cityid,object.stateid,object.name,object.code]
        self.params_list = list_params

    def post_update(self, object, returned_dict):
        city_model: CityModel = object
        return city_model

    def pre_delete(self, object: CityModel):
        self.sp_name = "sCityDelete"
        list_params = [object.cityid]
        self.params_list = list_params

    def post_delete(self, object, returned_dict):
        city_model: CityModel = object

        return city_model

    def pre_get(self, params):
        self.sp_name = "sCityGet"
        self.params_list = params.get_params_list()

    def post_get(self, cursor_object):
        if len(cursor_object.get_data()) > 0:
            city_model: CityModel = CityModel()
            for each_tuple in cursor_object.get_data():
                city_model.cityid = each_tuple[0]
                city_model.stateid = each_tuple[1]
                city_model.name = each_tuple[2]
                city_model.code = each_tuple[3]

            return city_model
        else:
            return None

    def pre_get_list(self, params):
        self.sp_name = "sCityGetList"
        self.params_list = params.get_params_list()

    def post_get_list(self, cursor_object):
        list_data = []
        if len(cursor_object.get_data()) > 0:
            for each_tuple in cursor_object.get_data():
                city_model: CityModel = CityModel()
                city_model.cityid = each_tuple[0]
                city_model.stateid = each_tuple[1]
                city_model.name = each_tuple[2]
                city_model.code = each_tuple[3]

                list_data.append(city_model)

            return list_data
        else:
            return None

    def pre_get_object(self, params):
        self.sp_name = "sCityObjectGet"
        self.params_list = params.get_params_list()

    def post_get_object(self, cursor_object):
        return self.post_get(cursor_object)

    def pre_get_list_object(self, params: ParamsObject):
        self.sp_name = "sCityObjectGetList"
        self.params_list = params.get_params_list()

    def post_get_list_object(self, cursor_object):
        return self.post_get_list(cursor_object)

    def pre_get_data_list_object_paginated(self, params):
        self.sp_name = "sCityGetListPage"
        self.params_list = params.get_params_list()

    def post_get_data_list_object_paginated(self, list_cursor_object):
        if len(list_cursor_object) > 0:
            object_list = self.post_get_list(list_cursor_object[1])
            return self.build_paginated_result(list_cursor_object[0], object_list)
        else:
            return None
