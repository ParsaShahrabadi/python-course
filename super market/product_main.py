
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from product_module import *
from datetime import date
import pickle


def total():
   try:
       messagebox.showinfo("Success", f"Total : {calculate_total(product_list)}")
   except Exception as e:
       messagebox.showinfo("Error", f"Error:{e}")

def reset_form():
    user_id.set(len(product_list)+1)
    name.set("")
    brand.set("")
    price.set(0)
    quantity.set(0)
    expire_date.set(str(date.today()))


def add():
    try:
        product = create_product_and_validat(user_id.get(),name.get(), brand.get(), quantity.get(), price.get(), expire_date.get())
        product_list.append(product)
        table.insert("",END,values=tuple(product.values()))
        reset_form()
        messagebox.showinfo("Success", "Products has been added")
    except Exception as e:
        messagebox.showerror("Save Error", f"Error : {e}")

def save():
    my_file = open("products","wb")
    pickle.dump(product_list,my_file)
    my_file.close()
    messagebox.showinfo("Success", "Products has been Saved")


def lode():
    my_file = open("products","rb")
    product_list = pickle.load(my_file)
    for product in product_list:
        table.insert("", END, values=tuple(product.values()))
    user_id.set(len(product_list)+1)


window = Tk()
window.title("Super Market")
window.geometry("800x380")

# id
Label(window, text="Id").place(x=25, y=25)
user_id = IntVar()
Entry(window, textvariable=user_id,state="readonly").place(x=120, y=25)

# name
Label(window, text="Name").place(x=25, y=65)
name = StringVar()
Entry(window, textvariable=name).place(x=120, y=65)

# brand
Label(window, text="Brand").place(x=25, y=105)
brand = StringVar()
Entry(window, textvariable=brand).place(x=120, y=105)

# quantity
Label(window, text="Quantity").place(x=25, y=145)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=120, y=145)

# price
Label(window, text="Price").place(x=25, y=185)
price = IntVar()
Entry(window, textvariable=price).place(x=120, y=185)

# expire_date
Label(window, text="Expiration Date\nYYYY-MM-DD").place(x=25, y=225)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=120, y=225)

Button(window, text="Add", command=add).place(x=145, y=280, width=100)
Button(window, text="Total", command=total).place(x=25, y=280, width=100)
Button(window, text="Lode" ,command=lode).place(x=25 , y= 320, width=100)
Button(window, text="save" ,command=save).place(x=145 , y= 320, width=100)

table = ttk.Treeview(window,columns=(1,2,3,4,5,6),height=15,show="headings")
table.heading(1,text="ID")
table.heading(2,text="Name")
table.heading(3,text="Brand")
table.heading(4,text="Quantity")
table.heading(5,text="Price")
table.heading(6,text="Expire Date")

table.column(1,width=50)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=60)
table.column(5,width=60)
table.column(6,width=100)

table.place(x=300, y=25)



reset_form()
window.mainloop()
