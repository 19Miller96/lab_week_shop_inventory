import unittest
from models.manufacturer import Manufacturer
from models.product import Product

if __name__ == "__main__":
    unittest.main()

class TestProduct(unittest.TestCase):
    
    def setup(self):
        self.product_1 = Product("banana", "a generic description", 100, 1, 2)

    def product_returns_name(self):
        self.assertEqual("banana", self.product_1.name)

