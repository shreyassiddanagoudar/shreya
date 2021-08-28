"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import branch_mapping
from django.urls import path

urlpatterns = [
    path("add", branch_mapping.add),
    path("update", branch_mapping.update),
    path("delete", branch_mapping.delete),
    path("get", branch_mapping.get),
    path("get-list", branch_mapping.get_list),
    path("get-object", branch_mapping.get_object),
    path("get-list-object", branch_mapping.get_list_object),
    path("get-list-object-page", branch_mapping.get_list_object_page),
]
