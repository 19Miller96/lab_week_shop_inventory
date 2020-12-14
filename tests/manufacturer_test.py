import unittest
from models.manufacturer import Manufacturer
from models.product import Product

if __name__ == "__main__":
    unittest.main()

class TestManufacturer(unittest.TestCase):
    
    def setup(self):
        self.manufacturer_1 = Manufacturer("Tesco")

    def manufacturer_returns_name(self):
        self.assertEqual("Tesco", self.manufacturer_1.name)