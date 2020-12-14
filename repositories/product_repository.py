from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product

def save(product):
    sql = "INSERT INTO products(name, description, stock_quantity, buying_cost, selling_cost) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.category]
    results = run_sql( sql, values )
    product.id = results[0]['id']
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product = Product(row['name'], row['description'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['description'], result['id'] )
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

# def products(manufacturer):
#     products = []
#     sql = "SELECT products.* FROM manufacturers INNER JOIN visits ON visits.user_id = users.id WHERE visits.location_id = %s"
#     values = [products.id]

#     results = run_sql(sql, values)

#     for row in results:
#         products = Products(row['name'], row['id'])
#         products.append(products)

#     return products
