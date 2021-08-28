"""
Created By : Nikesh
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import bs_subject_hdr_mapping
from django.urls import path

urlpatterns = [
    path("add", bs_subject_hdr_mapping.add),
    path("update", bs_subject_hdr_mapping.update),
    path("delete", bs_subject_hdr_mapping.delete),
    path("get", bs_subject_hdr_mapping.get),
    path("get-list", bs_subject_hdr_mapping.get_list),
    path("get-object", bs_subject_hdr_mapping.get_object),
    path("get-list-object", bs_subject_hdr_mapping.get_list_object),
    path("get-list-object-page", bs_subject_hdr_mapping.get_list_object_page),
]
