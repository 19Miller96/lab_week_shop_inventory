import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

product_1 = Product('Banana', 'A generic description', 20, 2, 3.50, "Tesco")
product_repository.save(product_1)

manufacturer_1 = Manufacturer('Tesco')
manufacturer_repository.save(manufacturer_1)

product_2 = Product('Apple', 'A healthy green fruit', 15, 1, 2, "Sainsburys")
product_repository.save(product_2)

manufacturer_2 = Manufacturer('Sainsburys')
manufacturer_repository.save(manufacturer_2)

product_3 = Product('Orange', 'A delicious fruit', 25, 1, 2, "Morrisons")
product_repository.save(product_3)

manufacturer_3 = Manufacturer('Morrisons')
manufacturer_repository.save(manufacturer_3)

product_4 = Product('Mango', 'Fresh from Australia', 60, 3, 4.50, "Tesco")
product_repository.save(product_4)

product_5 = Product('Kiwi', 'Not actually from New Zealand', 18, 2.50, 3.20, "Morrisons")
product_repository.save(product_5)

product_6 = Product('Avacado', 'Columbian Avacados', 80, 2, 4, "Sainsburys")
product_repository.save(product_6)

print(manufacturer_repository.products(manufacturer_1))
pdb.set_trace()

print(product_repository.manufacturers(product_1))
pdb.set_trace()
