import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

product1 = Product('Banana', 'A generic description', 20, 2, 3.50)
product_repository.save(product1)

manufacturer1 = Manufacturer('Tesco')
manufacturer_repository.save(manufacturer1)

# print(manufacturer_repository.products(manufacturer1))
# pdb.set_trace()

# print(product_repository.product(product1))
# pdb.set_trace()
