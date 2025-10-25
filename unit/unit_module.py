import re
from tkinter import messagebox
lessons_list = []

def code_validator(code):
    if not re.match("^[0-9]{1,4}$",code):
        raise ValueError("Invalid lesson code!!!")

def name_validator(name):
    if not re.match("^[a-zA-Z\s]{3,30}$",name):
        raise ValueError("invalid lesson name!!!")

def teacher_validator(teacher):
    if not re.match("^[a-zA-Z\s]{3,30}$",teacher):
        raise ValueError("invalid teacher name!!!")

def unit_validator(unit):
    if not re.match("[1-3]{1,5}",unit):
        raise ValueError("invalid unit!!!")

def save(code,name,teacher,unit):
    try:
        code_validator(code.get())
        name_validator(name.get())
        teacher_validator(teacher.get())
        unit_validator(unit.get())

        lessons = {"code":code.get(),
                   "name":name.get(),
                   "teacher":teacher.get(),
                   "unit":unit.get()}

        lessons_list.append(lessons)

        messagebox.showinfo("Success","Unit has been saved")
        code.set(0)
        name.set("")
        teacher.set("")
        unit.set(0)
    except Exception as e:
        messagebox.showerror("Save Error",f"Error : {e}")

