"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""


class ValidationHelper:

    def __init__(self):
        pass

    def is_none(self, data):
        if data is None:
            return True
        else:
            return False

    def is_string_empty_or_none(self, data):
        if data == "" or data is None:
            return True
        else:
            return False

    def is_valid_date(self, data):
        pass
