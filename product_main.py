from product_module import *

for i in range(5) :
    product = get_data()

    if product != None :
        product_list.append(product)
        print("save")
    else:
        print("invalid data!!!")

show_product(product_list)






