"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import subject_mapping
from django.urls import path

urlpatterns = [
    path("add", subject_mapping.add),
    path("update", subject_mapping.update),
    path("delete", subject_mapping.delete),
    path("get", subject_mapping.get),
    path("get-list", subject_mapping.get_list),
    path("get-object", subject_mapping.get_object),
    path("get-list-object", subject_mapping.get_list_object),
    path("get-list-object-page", subject_mapping.get_list_object_page),
]
