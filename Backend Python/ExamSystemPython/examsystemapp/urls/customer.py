"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import customer_mapping
from django.urls import path

urlpatterns = [
    path("add", customer_mapping.add),
    path("update", customer_mapping.update),
    path("delete", customer_mapping.delete),
    path("get", customer_mapping.get),
    path("get-list", customer_mapping.get_list),
    path("get-object", customer_mapping.get_object),
    path("get-list-object", customer_mapping.get_list_object),
    path("get-list-object-page", customer_mapping.get_list_object_page),
    path("customer-authentication", customer_mapping.customer_authentication),
]
