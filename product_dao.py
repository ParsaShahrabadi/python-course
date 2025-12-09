import sqlite3

class ProductDataAccecc:
    def save(self, product):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("insert into product (p_id,product_name,brand,quantity,expire_date,price,total) values (?, ?, ?, ?, ?, ?, ?)" ,
                           [product.p_id,
                            product.product_name,
                            product.brand,
                            product.quantity,
                            product.expire_date,
                            product.price,
                            product.total
                            ])

            connection.commit()

    def edit(self, product):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("update product set p_id=?, product_name=?, brand=? ,quantity=?, expire_date=?, price=?, total=?",
                           [product.p_id,
                            product.product_name,
                            product.brand,
                            product.quantity,
                            product.expire_date,
                            product.price,
                            product.total
                            ])
            connection.commit()

    def romove(self, p_id):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from product where p_id=?", [p_id])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from product order by name, brand")
            return cursor.fetchall()
