import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


import sys
from mlproject.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Constructs a detailed error message including file name, line number, and the actual error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] error message [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    """
    Custom Exception class to include detailed traceback info.
    """
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Keep base message for Exception
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message
