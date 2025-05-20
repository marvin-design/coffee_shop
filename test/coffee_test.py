import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def test_name_property(self):
        c = Coffee("Mocha")
        self.assertEqual(c.name, "Mocha")

        with self.assertRaises(ValueError):
            Coffee("A")

        with self.assertRaises(TypeError):
            Coffee(123)

    def test_coffee_orders_customers(self):
        c1 = Customer("Tom")
        c2 = Customer("Jerry")
        coffee = Coffee("Espresso")
        c1.create_order(coffee, 3.5)
        c2.create_order(coffee, 4.0)

        self.assertEqual(len(coffee.orders()), 2)
        self.assertIn(c1, coffee.customers())
        self.assertIn(c2, coffee.customers())

    def test_average_price(self):
        c = Customer("Ava")
        coffee = Coffee("Americano")
        self.assertEqual(coffee.average_price(), 0)

        c.create_orde_
