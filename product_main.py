
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from  product_controller import ProductsController
from matplotlib import pyplot as plt


#rest the entry and set id
def reset():
    product_name.set("")
    brand.set("")
    price.set(0)
    quantity.set(0)
    expire_date.set(str(datetime.now().date()))


    status, product_list = ProductsController.find_all()

    for item in table.get_children():
        table.delete(item)

    id_order = 0
    if status:
        for product in product_list:
            table.insert("", END, values=product)
            id_order = max(id_order, int(product[0]))
    else:
        messagebox.showerror("Error", product_list)
    p_id.set(id_order+1)


def select_product(event):
         product = table.item(table.focus())["values"]
         if product:
             p_id.set(product[0])
             product_name.set(product[1])
             brand.set(product[2])
             quantity.set(product[3])
             price.set(product[4])
             expire_date.set(product[5])

def save_click():
    status, message = ProductsController.save(
        p_id.get(),
        product_name.get(),
        brand.get(),
        quantity.get(),
        price.get(),
        expire_date.get(),

    )

    if status:
        reset()
        messagebox.showinfo("Save", message)
    else:
        messagebox.showerror("Error", message)

def edit_click():
    status, message = ProductsController.edit(
        p_id.get(),
        product_name.get(),
        brand.get(),
        quantity.get(),
        price.get(),
        expire_date.get()
    )

    if status:
        reset()
        messagebox.showinfo("Edit", message)
    else:
        messagebox.showerror("Error", message)

def remove_click():
    status, message = ProductsController.remove(p_id.get())


    if status:
        reset()
        messagebox.showinfo("remove", message)
    else:
        messagebox.showerror("Error", message)


def show_chart_click():
    status, data = ProductsController.get_chart_data()

    if not status:
        messagebox.showerror("Error", data)
        return

    names, quantities = data

    if not names:
        messagebox.showinfo("Chart", "No products in stock to display chart.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(names, quantities, color='skyblue')

    plt.xlabel("Product Name")
    plt.ylabel("Quantity in Stock")
    plt.title("Current Inventory Stock Levels")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()


def search_click():
    keyword = search_entry.get()
    for item in table.get_children():
        product = table.item(item)["values"]


        if product[1] == keyword or product[5] == keyword:
            table.selection_set(item)
            table.focus(item)
            table.see(item)
            return

    messagebox.showinfo("Search", "Item not found in the list!")


def calculate_total_click():
    total_sum = 0

    for item in table.get_children():
        product = table.item(item)["values"]
        total_sum += (product[6])
    discount = total_sum * 0.95
    if not 10000000 < total_sum:
        messagebox.showinfo("Total", f"Total Value of all product: {total_sum}")
    else:
        messagebox.showinfo("Total", f"Total Value of all product: {total_sum} \n discount 5% (; : {discount} ")
# ---------------------------------------------------------------------------------
window = Tk()
window.title("SMControl")
window.geometry("1070x458")
window.config(bg="#abcdef")

style = ttk.Style(window)
style.theme_use('clam')

# id
Label(window, text="ID",bg="#abcdef").place(x=25, y=25)
p_id = IntVar()
Entry(window, textvariable=p_id,state="readonly").place(x=120, y=25)

# name
Label(window, text="Item Name",bg="#abcdef").place(x=25, y=65)
product_name = StringVar()
Entry(window, textvariable=product_name).place(x=120, y=65)

# brand
Label(window, text="Brand",bg="#abcdef").place(x=25, y=105)
brand = StringVar()
Entry(window, textvariable=brand).place(x=120, y=105)

# quantity
Label(window, text="Quantity",bg="#abcdef").place(x=25, y=145)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=120, y=145)

# price
Label(window, text="Price",bg="#abcdef").place(x=25, y=185)
price = IntVar()
Entry(window, textvariable=price).place(x=120, y=185)

# expire_date
Label(window, text="Expire Date",bg="#abcdef").place(x=25, y=225)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=120, y=225)

# search
Label(window, text="Search Item:\n(Name or Date)", bg="#abcdef").place(x=290, y=420)
search_entry = StringVar()
Entry(window, textvariable=search_entry).place(x=380, y=422)


#buttons
Button(window, text="Save", width=30, command=save_click).place(x=25, y=260)
Button(window, text="Edit", width=30, command=edit_click).place(x=25, y=300)
Button(window, text="Remove", width=30, command=remove_click).place(x=25, y=380)
Button(window, text="Show Stock Chart", width=30, command=show_chart_click).place(x=25, y=340)
Button(window, text="Find", width=16, command=search_click).place(x=510, y=420)
Button(window, text="All Total", width=16, command=calculate_total_click).place(x=912, y=420)
#table in 7 column

table = ttk.Treeview(window,columns=("ID","Name","Brand","Quantity","Price","Expire Date","Total"),show="headings",height=18)


table.column("ID", width=50,anchor=CENTER)
table.column("Name", width=120,anchor=CENTER)
table.column("Brand", width=120,anchor=CENTER)
table.column("Quantity", width=100,anchor=CENTER)
table.column("Expire Date", width=120,anchor=CENTER)
table.column("Price", width=100,anchor=CENTER)
table.column("Total", width=120,anchor=CENTER)


table.heading("ID",text="ID")
table.heading("Name",text="Name")
table.heading("Brand",text="Brand")
table.heading("Quantity",text="Quantity")
table.heading("Price",text="Price")
table.heading("Expire Date",text="Expire Date")
table.heading("Total",text="Total")


table.place(x=300, y=25)
table.bind("<<TreeviewSelect>>", select_product)


reset()
window.mainloop()
