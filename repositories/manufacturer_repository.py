from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturers(name) VALUES (%s) RETURNING id"
    values = [manufacturer.name]
    results = run_sql( sql, values )
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['id'] )
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def products(manufacturer):
    products = []
    sql = "SELECT products.* FROM products INNER JOIN visits ON visits.product_id = products.id WHERE visits.manufacturer_id = %s"
    values = [manufacturer.id]

    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_cost'], row['id'])
        products.append(product)

    return products