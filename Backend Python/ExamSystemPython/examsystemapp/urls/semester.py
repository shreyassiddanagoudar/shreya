"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import semester_mapping
from django.urls import path

urlpatterns = [
    path("add", semester_mapping.add),
    path("update", semester_mapping.update),
    path("delete", semester_mapping.delete),
    path("get", semester_mapping.get),
    path("get-list", semester_mapping.get_list),
    path("get-object", semester_mapping.get_object),
    path("get-list-object", semester_mapping.get_list_object),
    path("get-list-object-page", semester_mapping.get_list_object_page),
]
