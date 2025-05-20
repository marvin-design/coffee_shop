from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = Order(alice, latte, 3.5)
order2 = Order(bob, latte, 4.5)
order3 = Order(alice, espresso, 5.0)

# Test Customer methods
assert alice.name == "Alice"
alice.name = "Alicia"
assert alice.name == "Alicia"

assert order1.customer == alice
assert order1.coffee == latte
assert order1.price == 3.5

assert latte.num_orders() == 2
assert abs(latte.average_price() - 4.0) < 0.01

assert alice.coffees() == [latte, espresso]
assert latte.customers() == [alice, bob]

# Test create_order
alice.create_order(latte, 4.0)
assert latte.num_orders() == 3

# Test bonus
aficionado = Customer.most_aficionado(latte)
assert aficionado == alice or aficionado == bob  # Depending on total spent

print("✅ All tests passed!")
