"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""


class CursorObject:

    def __init__(self, columns=[], data=()):
        self.columns = columns
        self.data = data

    def get_columns(self):
        return self.columns

    def get_data(self):
        return self.data
