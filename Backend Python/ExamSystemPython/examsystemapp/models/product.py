"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""
from examsystemapp.models.base_model import BaseModel
from examsystemapp.utils.helpers.general_helper import Validation


class ProductModel(BaseModel):
    def __init__(self, productid=None,name=None,description=None,brandid=None,imageurl=None,price=None,subcategoryid=None):
        self.productid = productid
        self.name = name
        self.description = description
        self.brandid = brandid
        self.imageurl = imageurl
        self.price = price
        self.subcategoryid = subcategoryid


    def get_id(self):
        return None

    def is_valid(self, type, event_type=None):
        return Validation()
