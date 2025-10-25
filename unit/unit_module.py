import re
from tkinter import messagebox
lessons_list = []

def code_validator(code):
    if not re.match("^[0-9]{1,4}$",str(code)):
        raise ValueError("Invalid lesson code!!!")

def name_validator(name):
    if not re.match("^[a-zA-Z\s]{3,30}$",name):
        raise ValueError("invalid lesson name!!!")

def teacher_validator(teacher):
    if not re.match("^[a-zA-Z\s]{3,30}$",teacher):
        raise ValueError("invalid teacher name!!!")

def unit_validator(unit):
    if not (type(unit) == int and unit in [1,2,3,5]):
        raise ValueError("invalid unit!!!")


