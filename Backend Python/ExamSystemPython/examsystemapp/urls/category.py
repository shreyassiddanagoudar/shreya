"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import category_mapping
from django.urls import path

urlpatterns = [
    path("add", category_mapping.add),
    path("update", category_mapping.update),
    path("delete", category_mapping.delete),
    path("get", category_mapping.get),
    path("get-list", category_mapping.get_list),
    path("get-object", category_mapping.get_object),
    path("get-list-object", category_mapping.get_list_object),
    path("get-list-object-page", category_mapping.get_list_object_page),
    path("get-menu", category_mapping.get_menu),
]
