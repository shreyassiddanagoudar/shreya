"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import state_mapping
from django.urls import path

urlpatterns = [
    path("add", state_mapping.add),
    path("update", state_mapping.update),
    path("delete", state_mapping.delete),
    path("get", state_mapping.get),
    path("get-list", state_mapping.get_list),
    path("get-object", state_mapping.get_object),
    path("get-list-object", state_mapping.get_list_object),
    path("get-list-object-page", state_mapping.get_list_object_page),
]
