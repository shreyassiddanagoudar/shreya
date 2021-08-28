"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import product_mapping
from django.urls import path

urlpatterns = [
    path("add", product_mapping.add),
    path("update", product_mapping.update),
    path("delete", product_mapping.delete),
    path("get", product_mapping.get),
    path("get-list", product_mapping.get_list),
    path("get-object", product_mapping.get_object),
    path("get-list-object", product_mapping.get_list_object),
    path("get-list-object-page", product_mapping.get_list_object_page),
    path("product-by-sub-cat", product_mapping.get_products_by_subcategory),
    path("product-by-search", product_mapping.get_products_by_search),
]
