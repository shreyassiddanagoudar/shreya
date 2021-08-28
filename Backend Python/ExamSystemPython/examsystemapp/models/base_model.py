"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

from abc import ABCMeta, abstractmethod


class BaseModel(metaclass=ABCMeta):
    OBJECT_TYPE = None

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def is_valid(self, type, event_type=None):
        pass
