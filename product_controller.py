import re
from datetime import datetime, date, time

from product_main import total
from product_modell import Products
from product_dao import ProductDataAccecc


class ProductsController:
    @staticmethod

    #validating products information
    def validator(name, brand, quantity, price, expire_date,):

        if not re.match("^[a-zA-Z\s]{3,30}$", name):
            raise ValueError("Invalid name")

        if not re.match("^[a-zA-Z0-9\s]{3,30}$", brand):
            raise ValueError("Invalid brand")

        if not price > 0:
            raise ValueError("Invalid price")

        if not quantity > 0:
            raise ValueError("Invalid quantity")

        try:
            datetime.strptime(expire_date, '%Y-%m-%d')
        except ValueError:
            raise NameError("Invalid expire format: yyyy-mm-dd")

        if datetime.now().date() > datetime.strptime(expire_date, '%Y-%m-%d'):
            raise NameError("Expier Date Padded")

        return True









