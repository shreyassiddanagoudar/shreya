"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import university_ay_mapping
from django.urls import path

urlpatterns = [
    path("add", university_ay_mapping.add),
    path("update", university_ay_mapping.update),
    path("delete", university_ay_mapping.delete),
    path("get", university_ay_mapping.get),
    path("get-list", university_ay_mapping.get_list),
    path("get-object", university_ay_mapping.get_object),
    path("get-list-object", university_ay_mapping.get_list_object),
    path("get-list-object-page", university_ay_mapping.get_list_object_page),
]
