import unittest
from models.manufacturer import Manufacturer
from models.product import Product

class TestManufacturer(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer_1 = Manufacturer("Tesco")

    def test_manufacturer_returns_name(self):
        self.assertEqual("Tesco", self.manufacturer_1.name)
