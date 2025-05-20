import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):

    def test_customer_name_setter_getter(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")
        c.name = "Bob"
        self.assertEqual(c.name, "Bob")
        with self.assertRaises(ValueError):
            c.name = ""  # too short
        with self.assertRaises(TypeError):
            c.name = 123

    def test_customer_create_order(self):
        c = Customer("Alice")
        coffee = Coffee("Latte")
        c.create_order(coffee, 4.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertEqual(c.orders()[0].price, 4.5)

    def test_customer_coffees_unique(self):
        c = Customer("Alice")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        c.create_order(coffee1, 4.5)
        c.create_order(coffee1, 5.0)
        c.create_order(coffee2, 3.5)
        self.assertEqual(set(c.coffees()), {coffee1, coffee2})

