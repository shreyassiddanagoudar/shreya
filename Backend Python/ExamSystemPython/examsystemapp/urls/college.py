"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import college_mapping
from django.urls import path

urlpatterns = [
    path("add", college_mapping.add),
    path("update", college_mapping.update),
    path("delete", college_mapping.delete),
    path("get", college_mapping.get),
    path("get-list", college_mapping.get_list),
    path("get-object", college_mapping.get_object),
    path("get-list-object", college_mapping.get_list_object),
    path("get-list-object-page", college_mapping.get_list_object_page),
]
