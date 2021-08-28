"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
from django.http import HttpRequest

from examsystemapp.api.base_controller import BaseController
from examsystemapp.utils.helpers.request_helper import RequestHelper
from django.conf import settings


class External(BaseController):

    def __init__(self, request: HttpRequest):
        BaseController.__init__(self, request)

    def check_session(self, request):
        pass

    def masters(self, request: HttpRequest):
        json_data = RequestHelper().call_ext_api(request, settings.MASTER_BASE_URL)
        return self.send_response_raw_json(json_data)
