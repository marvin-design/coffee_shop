import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_order_initialization(self):
        c = Customer("John")
        coffee = Coffee("Latte")
        order = Order(c, coffee, 5.0)

        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_order_invalid_price(self):
        c = Customer("Jane")
        coffee = Coffee("Cappuccino")

        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(c, coffee, 11.0)

        with self.assertRaises(ValueError):
            Order(c, coffee, "Free")

    def test_order_invalid_types(self):
        with self.assertRaises(TypeError):
            Order("Alice", Coffee("Latte"), 3.0)

        with self.assertRaises(TypeError):
            Order(Customer("Alice"), "Latte", 3.0)

if __name__ == "__main__":
    unittest.main()
