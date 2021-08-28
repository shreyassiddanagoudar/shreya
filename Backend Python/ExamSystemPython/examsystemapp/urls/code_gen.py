"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

from .url_mapping import code_gen_mapping
from django.urls import path

urlpatterns = [
    path("generate", code_gen_mapping.generate_code),
]
