"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import order_mapping
from django.urls import path

urlpatterns = [
    path("add", order_mapping.add),
    path("update", order_mapping.update),
    path("delete", order_mapping.delete),
    path("get", order_mapping.get),
    path("get-list", order_mapping.get_list),
    path("get-object", order_mapping.get_object),
    path("get-list-object", order_mapping.get_list_object),
    path("get-list-object-page", order_mapping.get_list_object_page),
]
