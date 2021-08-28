"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import city_mapping
from django.urls import path

urlpatterns = [
    path("add", city_mapping.add),
    path("update", city_mapping.update),
    path("delete", city_mapping.delete),
    path("get", city_mapping.get),
    path("get-list", city_mapping.get_list),
    path("get-object", city_mapping.get_object),
    path("get-list-object", city_mapping.get_list_object),
    path("get-list-object-page", city_mapping.get_list_object_page),
]
