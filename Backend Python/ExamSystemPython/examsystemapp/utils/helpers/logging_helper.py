"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""

import logging
import threading


class LogItem:
    def __init__(self, log_class=None, log_message=None, log_object=None):
        self.log_class = log_class
        self.log_message = log_message
        self.log_object = log_object


class LoggingHelper:
    def __init__(self):
        pass

    def log(self, log_class=None, log_message=None, log_object=None, log_type="DEBUG"):
        log = LogItem(log_class, log_message, log_object).__dict__
        if log_type == "DEBUG":
            logging.getLogger('debug_log').debug(log)
        else:
            logging.getLogger('error_log').error(log)

    def log_debug(self, log_class=None, log_message=None, log_object=None):
        t1 = threading.Thread(target=self.log, args=(log_class, log_message, log_object, "DEBUG"))
        t1.start()
        # self.log(log_class, log_message, log_object)

    def log_error(self, log_class=None, log_message=None, log_object=None):
        t1 = threading.Thread(target=self.log, args=(log_class, log_message, log_object, "ERROR"))
        t1.start()
        # self.log(log_class, log_message, log_object, "ERROR")
