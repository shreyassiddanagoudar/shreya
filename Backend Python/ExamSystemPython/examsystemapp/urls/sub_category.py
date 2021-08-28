"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import sub_category_mapping
from django.urls import path

urlpatterns = [
    path("add", sub_category_mapping.add),
    path("update", sub_category_mapping.update),
    path("delete", sub_category_mapping.delete),
    path("get", sub_category_mapping.get),
    path("get-list", sub_category_mapping.get_list),
    path("get-object", sub_category_mapping.get_object),
    path("get-list-object", sub_category_mapping.get_list_object),
    path("get-list-object-page", sub_category_mapping.get_list_object_page),
]
