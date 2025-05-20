import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):

    def test_coffee_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")
        c = Coffee("Espresso")
        self.assertEqual(c.name, "Espresso")
        with self.assertRaises(AttributeError):
            c.name = "Latte"  # name is immutable

    def test_num_orders_and_avg_price(self):
        c1 = Customer("Alice")
        coffee = Coffee("Mocha")
        c1.create_order(coffee, 5.0)
        c1.create_order(coffee, 7.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.average_price(), 6.0)

    def test_unique_customers(self):
        coffee = Coffee("Americano")
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        c1.create_order(coffee, 5.0)
        c2.create_order(coffee, 6.0)
        self.assertEqual(set(coffee.customers()), {c1, c2})

