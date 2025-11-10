from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from lesson import Lesson
from university import SumUnit

term = SumUnit(1)


def reset_form():
    code.set(0)
    name.set("")
    teacher.set("")
    unit.set(0)


def save():
    try:
        lesson = Lesson(code.get(), name.get(), teacher.get(), unit.get())

        lesson.is_valid()
        term.add_unit(lesson)
        table.insert("", END, values=lesson.to_tuple())
        reset_form()
        messagebox.showinfo("Success", "Unit has been saved")
    except Exception as e:
        messagebox.showerror("Save Error", f"Error : {e}")
def total():
    try:
        if 12 <= term.total_unit() <=24:
            messagebox.showinfo("Total Unit", f"Total Unit: : {term.total_unit()}")
        else:
            messagebox.showinfo("Unit limit", f"Total Unit Must Be Above 12 And Under 24\n Your Total Unit: {term.total_unit()}")
    except Exception as e:
        messagebox.showinfo("Error",f"Error: {e}")


window = Tk()
window.title("unit selection")
window.geometry("620x380")

# lesson_code
Label(window, text="Lesson Code").place(x=30, y=25)
code = IntVar()
Entry(window, textvariable=code).place(x=115, y=25)

# lesson_name
Label(window, text="Lesson Name").place(x=30, y=50)
name = StringVar()
Entry(window, textvariable=name).place(x=115, y=50)

# lesson_teacher
Label(window, text="Lesson Teacher").place(x=30, y=75)
teacher = StringVar()
Entry(window, textvariable=teacher).place(x=115, y=75)

# lesson_unit
Label(window, text="Lesson Unit").place(x=30, y=100)
unit = IntVar()
Entry(window, textvariable=unit).place(x=115, y=100)

Button(window, text="Save", command=save).place(x=115, y=130, width=125)
Button(window, text="Total", command=total).place(x=115, y=160, width=125)

table = ttk.Treeview(window,columns=(1,2,3,4),height=15,show="headings")

table.heading(1,text="Code")
table.heading(2,text="Name")
table.heading(3,text="Teacher")
table.heading(4,text="Unit")

table.column(1,width=60)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=40)

table.place(x=280, y=25)

window.mainloop()
