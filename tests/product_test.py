import unittest
from models.manufacturer import Manufacturer
from models.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.product_1 = Product("banana", "a generic description", 100, 1, 2, "Tesco")

    def test_product_returns_name(self):
        self.assertEqual("banana", self.product_1.name)

    def test_product_returns_description(self):
        self.assertEqual("a generic description", self.product_1.description)
    
    def test_product_returns_stock_quantity(self):
        self.assertEqual(100, self.product_1.stock_quantity)

    def test_product_returns_buying_cost(self):
        self.assertEqual(1, self.product_1.buying_cost)

    def test_product_returns_selling_cost(self):
        self.assertEqual(2, self.product_1.selling_cost)

    def test_product_returns_profit(self):
        self.assertEqual(1, self.product_1.selling_cost - self.product_1.buying_cost)

    def test_product_returns_manufacturer(self):
        self.assertEqual("Tesco", self.product_1.manufacturer)