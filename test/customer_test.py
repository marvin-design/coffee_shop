import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_name_getter_setter(self):
        c = Customer("Anna")
        self.assertEqual(c.name, "Anna")

        c.name = "Ben"
        self.assertEqual(c.name, "Ben")

        with self.assertRaises(ValueError):
            c.name = ""

        with self.assertRaises(ValueError):
            c.name = "ThisNameIsWayTooLong"

        with self.assertRaises(TypeError):
            c.name = 123

    def test_customer_orders_and_coffees(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        c.create_order(coffee, 5.0)
        
