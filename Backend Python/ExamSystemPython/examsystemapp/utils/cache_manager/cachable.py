"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

from abc import ABC


class ICachable(ABC):

    def get_cache_key(self):
        pass

    def is_commons_cacheable(self):
        return True
