"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

import datetime
from PIL import Image
from fuzzywuzzy import fuzz


class Validation:
    def __init__(self, is_valid=True, validation_message="Not a valid Object", validation_object=None):
        self.is_valid = is_valid
        self.validation_message = validation_message
        self.validation_object = validation_object


class IntHelper:

    @staticmethod
    def string_to_int(string_value, default_value=None):
        return default_value if string_value == "" or string_value is None else int(string_value)


class FloatHelper:

    @staticmethod
    def string_to_float(string_value, default_value=None):
        return default_value if string_value == "" or string_value is None else float(string_value)


class StringHelper:

    @staticmethod
    def cast_string(string_value):
        return None if string_value is None else str(string_value)

    @staticmethod
    def isvalid(string_value):
        if string_value == '' or string_value is None or type(string_value) != str:
            return False
        else:
            return True

    @staticmethod
    def length(string_value):
        if StringHelper.isvalid(string_value):
            return len(string_value)
        else:
            return None

    @staticmethod
    def toUpper(string_value):
        if StringHelper.isvalid(string_value):
            return string_value.upper()
        else:
            return None

    @staticmethod
    def toLower(string_value):
        if StringHelper.isvalid(string_value):
            return string_value.lower()
        else:
            return None

    @staticmethod
    def replace(string_value, source_str, replace_str):
        if StringHelper.isvalid(source_str) and StringHelper.isvalid(replace_str):
            return string_value.replace(source_str, replace_str)
        else:
            return None

    @staticmethod
    def trim(string_value, left=True, right=True):
        if StringHelper.isvalid(string_value):

            if left == True and right == True:
                x = string_value.lstrip().rstrip()

            elif left == True and right == False:
                x = string_value.lstrip()

            elif right == True and left == True:
                x = string_value.rstrip()

            else:
                x = string_value
            return x
        else:
            return None

    @staticmethod
    def remove_spl_characters(x):
        return x \
            .replace(' ', '') \
            .replace('.', '') \
            .replace('/', '') \
            .replace('-', '') \
            .replace(':', '') \
            .replace(',', '') \
            .replace('(', '') \
            .replace(')', '') \
            .lower()

    @staticmethod
    def find_similarity_percentage(s1, s2):
        return fuzz.ratio(s1, s2)


class DateHelper:

    def __init__(self):
        pass

    # ------------------------------------------------------------------------------------------ #

    """
    :description : used to get current_time[Ex: datetime.time(11, 8, 25)] or
                    current_time_with_ milliseconds[Ex:datetime.datetime( 11, 51, 13, 848913)]
    :param  with_millisec default: False (date) 
    :returns dateobject ot date_time_object

    """

    @staticmethod
    def get_current_time(with_millisec=False):
        if with_millisec:
            return datetime.datetime.now().time()
        else:
            return datetime.datetime.now().time().replace(microsecond=0)  # returns time object

    # ------------------------------------------------------------------------------------------ #
    """
    :description : used to get current_date[Ex: datetime.time(11, 8, 25)] or
                    current_date_with_time[Ex:datetime.datetime(2019, 6, 6, 11, 51, 13, 848913)]
    :param  with_millisec default: False (date) if True (datetime)
    :returns dateobject ot date_time_object

    """

    @staticmethod
    def get_current_date(with_millisec=False):
        if with_millisec:
            return datetime.datetime.now()
        else:
            return datetime.datetime.now().date()  # returns date object

    # ------------------------------------------------------------------------------------------ #

    #             "Date"   - "format"
    #         "2019-04-08" - "%Y-%m-%d"
    #         "04-08-2018" - "%d-%m-%Y"
    #         "04-08-18"   - "%d-%m-%y"

    """
    :description : used to convert string to date object 
    :param  input_date (in string) and  date_format (in string)
    :returns dateobject 

    """

    @staticmethod
    def convert_string_to_date_object(input_date_as_string, date_format):
        try:
            x = datetime.datetime.strptime(input_date_as_string, date_format).date()
        except ValueError:
            x = None

        return x  # returns date object

    # ------------------------------------------------------------------------------------------ #

    #             "Date"   - "format"
    #         "2019-04-08" - "%Y-%m-%d"
    #         "04-08-2018" - "%d-%m-%Y"
    #         "04-08-18"   - "%d-%m-%y"

    """
    :description : used to convert date object to string 
    :param  input_date (in date_object) and  output_format (in string )
    :returns date as string 

    """

    @staticmethod
    def convert_date_object_to_string(date, output_format):
        yyyymmdd = str(date)
        if output_format == "%Y-%m-%d":
            return yyyymmdd
        elif output_format == "%d-%m-%Y":
            ddmmyyyy = yyyymmdd[8:10] + '-' + yyyymmdd[5:7] + '-' + yyyymmdd[0:4]
            return ddmmyyyy
        elif output_format == "%d-%m-%y":
            ddmmyy = yyyymmdd[8:10] + '-' + yyyymmdd[5:7] + '-' + yyyymmdd[2:4]
            return ddmmyy
        else:
            return None

    # ------------------------------------------------------------------------------------------ #

    """
    :description : used to add number_of_days to input datetime object 
    :param  input_date (in date_object) and  output_format (in string )
    :returns date as string 

    """

    @staticmethod
    def date_add(input_date_time, number_of_days):
        return (input_date_time + datetime.timedelta(days=number_of_days)).date()  # returns date object

        # input_date_time should be datetime object

    # ------------------------------------------------------------------------------------------ #

    """
    :description : used to check if date is valid
    :param  input_date (in string) and  input_format (in string )
    :returns True/False

    """

    @staticmethod
    def is_Valid(input_date, input_format):
        try:
            datetime.datetime.strptime(input_date, input_format).date()
            x = True
        except ValueError:
            x = False
        return x


class ImageHelper:

    @staticmethod
    def compress_image(imagepath):
        im = Image.open(imagepath)
        im.save(imagepath, optimize=True, quality=25)
