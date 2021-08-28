"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import student_ay_mapping
from django.urls import path

urlpatterns = [
    path("add", student_ay_mapping.add),
    path("update", student_ay_mapping.update),
    path("delete", student_ay_mapping.delete),
    path("get", student_ay_mapping.get),
    path("get-list", student_ay_mapping.get_list),
    path("get-object", student_ay_mapping.get_object),
    path("get-list-object", student_ay_mapping.get_list_object),
    path("get-list-object-page", student_ay_mapping.get_list_object_page),
]
