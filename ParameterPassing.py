"""
    Different types of arguments
    1. Positional Arguments
    2. Keyword Arguments
    3. Default Arguments
    4. Arbitrary Positional Arguments
    5. Arbitrary Keyword Arguments
"""

# Import libraries
import sys
from datetime import datetime


# User defined function
"""
Input Arguments:
    date: Current date and time
    msg: Message to be printed
    mytype: Message type
    *arguments: Arbitrary positional arguments
    **kwargs: Arbitrary keyword arguments
"""
def logger(msg, mytype):
    print(f" [{datetime.now()}] [{mytype}] - {msg}")

def logger_with_default_arg(msg, mytype="INFO"):
    print(f" [{datetime.now()}] [{mytype}] - {msg}")

def logger_with_arbitrary_pos_arg(*arguments):
    print(f"[{arguments[1]}] [{arguments[0]}] - [{arguments[2]}] - [{arguments[3:]}]")

def logger_with_arbitrary_keyword_arg(**kwargs):
    msg = None
    mytype = None
    for key, value in kwargs.items():
        if key == "msg":
            msg = value
        elif key == "mytype":
            mytype = value

    print(f" [{datetime.now()}] [{mytype}] - {msg} - {kwargs}")

# Entry point function
def main():

    logger("Testing positional arguments", "INFO")
    logger(mytype="DEBUG", msg="Testing keyword arguments")

    logger_with_default_arg("Testing default argument")          # mytype will take default value "INFO"
    logger_with_default_arg("Testing default argument", "FATAL") # mytype will take value "FATAL" unless default value is overridden

    logger_with_arbitrary_pos_arg(datetime.now(), "Testing Arbitrary Positional Arguments", "INFO", 1, 2, 3, 4, 5) # arguments will take all positional arguments as a tuple

    logger_with_arbitrary_keyword_arg(datetime= datetime.now(), msg="Testing Arbitary Keyword Arguments", mytype="INFO", id=1, name="Test") # kwargs will take key-value pairs

    sys.exit(0)

# Call main
main()