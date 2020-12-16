import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

manufacturer_1 = Manufacturer('Tesco')
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer('Morrisons')
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer('Sainsburys')
manufacturer_repository.save(manufacturer_3)

manufacturer_4 = Manufacturer('Asda')
manufacturer_repository.save(manufacturer_4)

product_1 = Product('Banana', 'A generic description', 20, 2, 4, manufacturer_1)
product_repository.save(product_1)

product_2 = Product('Apple', 'A healthy green fruit', 15, 1, 2, manufacturer_2)
product_repository.save(product_2)

product_3 = Product('Orange', 'A delicious fruit', 25, 1, 2, manufacturer_3)
product_repository.save(product_3)

print(manufacturer_repository.products(manufacturer_1))
pdb.set_trace()

print(product_repository.manufacturers(product_1))
pdb.set_trace()
