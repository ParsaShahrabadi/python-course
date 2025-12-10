import sqlite3

class ProductDataAccecc:
    def save(self, product):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("insert into products (p_id,product_name,brand,quantity,expire_date,price,total)" "values (?, ?, ?, ?, ?, ?, ?)" ,
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
            cursor.execute("update products set product_name=?, brand=? ,quantity=?, expire_date=?, price=?, total=?""where p_id=?",
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
            cursor.execute("delete from products where p_id=?", [p_id])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from products order by product_name, brand")
            return cursor.fetchall()

