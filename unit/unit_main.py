from tkinter import *
from unit_module import *
window = Tk()
window.title("unit selection")
window.geometry("500x500")

#lesson_code
Label(window, text="lesson_code").place(x = 150, y = 25)
code = IntVar()
Entry(window,textvariable=code).place(x = 230,y = 25)

#lesson_name
Label(window, text="lesson_name").place(x = 150, y = 50)
name = StringVar()
Entry(window,textvariable=name).place(x = 230,y = 50)

#lesson_teacher
Label(window, text="lesson_teacher").place(x = 150, y = 75)
teacher = StringVar()
Entry(window, textvariable=teacher).place(x = 230 , y =75 )

#lesson_unit
Label(window, text="lesson_unit").place(x = 150 , y = 100)
unit = IntVar()
Entry(window, textvariable=unit).place(x = 230 , y = 100)

Button(window,text="Save",command = lambda:save(code,name,teacher,unit)).place(x = 155, y = 150, width = 200)








window.mainloop()
