from product_module import *

while total != None :
    product = get_data()

    if product != None :
        product_list.append(product)
        print("save")
    else:
        print("invalid data!!!")
    limit(product)

show_product(product_list)






