import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        c = Customer("Gyavira")
        coffee = Coffee("Azaria")
        o = Order(c, coffee, 4.5)
        self.assertEqual(o.customer, c)
        self.assertEqual(o.coffee, coffee)
        self.assertEqual(o.price, 4.5)

    def test_invalid_price(self):
        c = Customer("Elyanna")
        coffee = Coffee("Vanestrol")
        with self.assertRaises(ValueError):
            Order(c, coffee, 15.0)

if __name__ == "__main__":
    unittest.main()