"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import staff_mapping
from django.urls import path

urlpatterns = [
    path("add", staff_mapping.add),
    path("update", staff_mapping.update),
    path("delete", staff_mapping.delete),
    path("get", staff_mapping.get),
    path("get-list", staff_mapping.get_list),
    path("get-object", staff_mapping.get_object),
    path("get-list-object", staff_mapping.get_list_object),
    path("get-list-object-page", staff_mapping.get_list_object_page),
]
