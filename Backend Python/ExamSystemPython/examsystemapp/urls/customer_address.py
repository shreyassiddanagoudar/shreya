"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import customer_address_mapping
from django.urls import path

urlpatterns = [
    path("add", customer_address_mapping.add),
    path("update", customer_address_mapping.update),
    path("delete", customer_address_mapping.delete),
    path("get", customer_address_mapping.get),
    path("get-list", customer_address_mapping.get_list),
    path("get-object", customer_address_mapping.get_object),
    path("get-list-object", customer_address_mapping.get_list_object),
    path("get-list-object-page", customer_address_mapping.get_list_object_page),
    path("get-customer-adderss-by-id", customer_address_mapping.get_list_customer_adderss_by_id),
]
