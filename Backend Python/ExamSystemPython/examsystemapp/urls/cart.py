"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import cart_mapping
from django.urls import path

urlpatterns = [
    path("add", cart_mapping.add),
    path("update", cart_mapping.update),
    path("delete", cart_mapping.delete),
    path("get", cart_mapping.get),
    path("get-list", cart_mapping.get_list),
    path("get-object", cart_mapping.get_object),
    path("get-list-object", cart_mapping.get_list_object),
    path("get-list-object-page", cart_mapping.get_list_object_page),
    path("delete-item", cart_mapping.delete_item),
    path("update-item", cart_mapping.update_item),
]
