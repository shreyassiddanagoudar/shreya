"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""


class DataObject:

    def __init__(self, list_objects=[], list_dict=[], list_json=[]):
        self.list_objects: list = list_objects
        self.list_dict: list = list_dict
        self.list_json: list = list_json

    def get_list_objects(self):
        return self.list_objects

    def get_list_dict(self):
        return self.list_dict

    def get_list_json(self):
        return self.list_json

    def get_one_object(self):
        return self.list_objects[0]

    def get_one_dict(self):
        return self.list_dict[0]

    def get_one_json(self):
        return self.list_json[0]
