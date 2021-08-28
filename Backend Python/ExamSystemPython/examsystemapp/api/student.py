"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
import json
from django.http import HttpRequest
from examsystemapp.api.base_controller import BaseController
from examsystemapp.models.student import StudentModel
from examsystemapp.services.student_service import StudentService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType, AppConstants
from examsystemapp.utils.helpers.general_helper import IntHelper, FloatHelper
from examsystemapp.utils.helpers.request_helper import RequestConfig, ParamsObject


class Student(BaseController):

    def __init__(self, request):
        BaseController.__init__(self, request)

    def add(self, request: HttpRequest):
        student_json = json.loads(request.POST.get("student_json"))

        student_object: StudentModel = StudentModel()
    
        student_object.collegeid = student_json.get("collegeid")
        student_object.branchid = student_json.get("branchid")
        student_object.currentsemester = student_json.get("currentsemester")
        student_object.name = student_json.get("name")
        student_object.rollno = student_json.get("rollno")
        student_object.add1 = student_json.get("add1")
        student_object.add2 = student_json.get("add2")
        student_object.add3 = student_json.get("add3")
        student_object.cityid = student_json.get("cityid")
        student_object.stateid = student_json.get("stateid")
        student_object.pin = student_json.get("pin")
        student_object.phonenum = student_json.get("phonenum")
        student_object.email = student_json.get("email")
        student_object.profilepic = student_json.get("profilepic")
        student_object.loginid = student_json.get("loginid")
        student_object.passwd = student_json.get("passwd")

        student_service: StudentService = StudentService()
        student_object = student_service.add(student_object)

        return self.send_response(student_object)

    def update(self, request: HttpRequest):
        student_json = json.loads(request.POST.get("student_json"))

        student_object: StudentModel = StudentModel()
        student_object.studentid = student_json.get("studentid")
        student_object.collegeid = student_json.get("collegeid")
        student_object.branchid = student_json.get("branchid")
        student_object.currentsemester = student_json.get("currentsemester")
        student_object.name = student_json.get("name")
        student_object.rollno = student_json.get("rollno")
        student_object.add1 = student_json.get("add1")
        student_object.add2 = student_json.get("add2")
        student_object.add3 = student_json.get("add3")
        student_object.cityid = student_json.get("cityid")
        student_object.stateid = student_json.get("stateid")
        student_object.pin = student_json.get("pin")
        student_object.phonenum = student_json.get("phonenum")
        student_object.email = student_json.get("email")
        student_object.profilepic = student_json.get("profilepic")
        student_object.loginid = student_json.get("loginid")
        student_object.passwd = student_json.get("passwd")

        student_service: StudentService = StudentService()
        student_object = student_service.update(student_object)

        return self.send_response(student_object)

    def delete(self, request: HttpRequest):
        student_json = json.loads(request.POST.get("student_json"))

        student_object: StudentModel = StudentModel()
        student_object.studentid = student_json.get("studentid")
       
        student_service: StudentService = StudentService()
        student_object = student_service.delete(student_object)

        return self.send_response(student_object)

    def get(self, request: HttpRequest):
        params = [
            {"id": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.INT)}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_service: StudentService = StudentService()
        data = student_service.get(params)
        return self.send_response(data)

    def get_list(self, request: HttpRequest):
        params = [
            {"ids": RequestConfig(from_session=False, nullable=False, datatype=DataTypes.STRING, default='')}
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_service: StudentService = StudentService()
        data = student_service.get_list(params)
        return self.send_response(data)

    def get_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_service: StudentService = StudentService()
        data = student_service.get_object(params)
        return self.send_response(data)

    def get_list_object(self, request: HttpRequest):
        params = []
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_service: StudentService = StudentService()
        data = student_service.get_list_object(params)
        return self.send_response(data)

    def get_list_object_page(self, request: HttpRequest):
        params = [
            {"collegeID": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"branchID": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=None)},
            {"currentSemester": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=None)},
            {"studentName": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=None)},
            {"rollNo": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=None)},
            {"page_Num": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.INT, default=1)},
            {"page_Size": RequestConfig(from_session=False, nullable=True, datatype=DataTypes.STRING, default=10)}
            
        ]
        params: ParamsObject = self.convert_params(request, HttpMethodType.get, params)
        student_service: StudentService = StudentService()
        data = student_service.get_list_object_paginated(params)
        return self.send_response(data)
