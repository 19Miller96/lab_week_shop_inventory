import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

product_1 = Product("Banana", "A generic description", 20, 2, 4, "Tesco")
product_repository.save(product_1)

manufacturer_1 = Manufacturer('Tesco')
manufacturer_repository.save(manufacturer_1)

product_2 = Product('Apple', 'A healthy green fruit', 15, 1, 2, 'Sainsburys')
product_repository.save(product_2)

manufacturer_2 = Manufacturer('Sainsburys')
manufacturer_repository.save(manufacturer_2)

product_3 = Product('Orange', 'A delicious fruit', 25, 1, 2, 'Morrisons')
product_repository.save(product_3)

manufacturer_3 = Manufacturer('Morrisons')
manufacturer_repository.save(manufacturer_3)

product_4 = Product('Mango', 'Fresh from Australia', 60, 3, 5, 'Tesco')
product_repository.save(product_4)

product_5 = Product('Kiwi', 'Not actually from New Zealand', 18, 3, 4, 'Morrisons')
product_repository.save(product_5)

product_6 = Product('Avacado', 'Columbian Avacados', 80, 2, 4, 'Sainsburys')
product_repository.save(product_6)

product_7 = Product('Watermelon', '10% melon, 90% water', 50, 3, 4, 'Tesco')
product_repository.save(product_7)

product_8 = Product('Pineapple', 'Contains neithers pines nor apples', 40, 10, 20, 'Morrisons')
product_repository.save(product_8)

product_9 = Product('Tangerine', 'Like a smaller version of an orange', 35, 2, 5, 'Sainsburys')
product_repository.save(product_9)

product_10 = Product('Passionfruit', 'The very fruit that inspired Drake', 1, 10, 10000, 'Tesco')
product_repository.save(product_10)

product_11 = Product('Grapes', 'Fresh from the coast of africa', 25, 8, 12, 'Morrisons')
product_repository.save(product_11)

product_12 = Product('Strawberries', 'Straight from Australia', 50, 3, 5, 'Tesco')
product_repository.save(product_12)

product_13 = Product('Pomegranate', 'Originally from Iran, now in your local Tesco', 30, 4, 6, 'Tesco')
product_repository.save(product_13)

product_14 = Product('Melon', '90% more melon than a watermelon', 45, 3, 6, 'Sainsburys')
product_repository.save(product_14)

product_15 = Product('Papaya', 'Fresh from spain', 85, 5, 7, 'Morrisons')
product_repository.save(product_15)

product_16 = Product('Raspberry', 'Voted the best berry of 2019', 35, 1, 2, 'Sainsburys')
product_repository.save(product_16)

product_17 = Product('Blackberry', 'Voted the best berry of 2018', 50, 4, 6, 'Tesco')
product_repository.save(product_17)

product_18 = Product('Blueberry', "The number one berry for baking", 35, 2, 3, 'Tesco')
product_repository.save(product_18)

product_19 = Product('Cranberry', 'Perhaps the blacksheep of the berry family', 60, 2, 8, 'Morrisons')
product_repository.save(product_19)

product_20 = Product('Lemon', 'Can be used as both a cooking ingredient and an insult', 86, 1, 3, 'Sainsburys')
product_repository.save(product_20)

print(manufacturer_repository.products(manufacturer_1))
pdb.set_trace()

print(product_repository.manufacturers(product_1))
pdb.set_trace()
