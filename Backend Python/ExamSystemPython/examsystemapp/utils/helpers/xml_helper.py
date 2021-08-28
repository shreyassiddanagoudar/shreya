"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

import xmltodict


class XmlConverter:
    def __init__(self):
        pass

    def convert_in_list(self, list_object: list, keys: list):
        updated_data = []
        for each_object in list_object:
            for each_key in keys:
                xml_data = each_object[each_key]
                if xml_data != "" and xml_data is not None:
                    xml_to_dict = xmltodict.parse(xml_data, dict_constructor=dict)
                    each_object[each_key] = xml_to_dict
                    updated_data.append(each_object)
        return updated_data

    def convert_in_dict(self, dict_object: dict, keys: list):
        for each_key in keys:
            xml_data = dict_object[each_key]
            if xml_data != "" and xml_data is not None:
                xml_to_dict = xmltodict.parse(xml_data, dict_constructor=dict)
                dict_object[each_key] = xml_to_dict
        return dict_object
