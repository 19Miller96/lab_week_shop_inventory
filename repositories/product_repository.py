from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product

def save(product):
    sql = "INSERT INTO products(name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_cost, product.manufacturer.id]
    results = run_sql( sql, values )
    product.id = results[0]['id']
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_cost'], row['manufacturer_id'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['name'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_cost'], result['manufacturer_id'], result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def manufacturers(product):
    manufacturers = []
    sql = "SELECT manufacturers.* FROM manufacturers"
    values = [product.id]

    results = run_sql(sql, values)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)

    return manufacturers

def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_cost, product.manufacturer.id, product.id]
    run_sql(sql, values)
