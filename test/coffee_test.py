import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_valid_and_invalid_name(self):
        c = Customer("Elyanna")
        self.assertEqual(c.name, "Elyanna")
        with self.assertRaises(ValueError):
            Customer("")  # Too short

    def test_name_setter(self):
        c = Customer("Carlson")
        c.name = "Azaria"
        self.assertEqual(c.name, "Azaria")
        with self.assertRaises(ValueError):
            c.name = ""  # Invalid

if __name__ == "__main__":
    unittest.main()