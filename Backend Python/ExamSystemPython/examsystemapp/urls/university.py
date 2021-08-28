"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import university_mapping
from django.urls import path

urlpatterns = [
    path("add", university_mapping.add),
    path("update", university_mapping.update),
    path("delete", university_mapping.delete),
    path("get", university_mapping.get),
    path("get-list", university_mapping.get_list),
    path("get-object", university_mapping.get_object),
    path("get-list-object", university_mapping.get_list_object),
    path("get-list-object-page", university_mapping.get_list_object_page),
]
