import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_order_initialization(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(c, coffee, 6.5)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 6.5)

    def test_invalid_price(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)
        with self.assertRaises(TypeError):
            Order(c, coffee, "cheap")

