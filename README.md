# coffee_shop

---

## 📦 Features

### ✅ Models & Properties

- **Customer**
  - Stores a name (string, 1–15 characters)
  - `name` is a property with getter and setter

- **Coffee**
  - Stores a name (string, min 3 characters)
  - `name` is immutable after initialization

- **Order**
  - Accepts a Customer, a Coffee, and a price (float between 1.0 and 10.0)
  - `price` is immutable

---

### 🔗 Object Relationships

- `Order.customer` → Returns Customer instance
- `Order.coffee` → Returns Coffee instance
- `Customer.orders()` → All orders by customer
- `Customer.coffees()` → Unique coffees ordered by customer
- `Coffee.orders()` → All orders of this coffee
- `Coffee.customers()` → Unique customers who ordered the coffee

---

### 📊 Aggregates

- `Customer.create_order(coffee, price)`
- `Coffee.num_orders()` → Total number of orders
- `Coffee.average_price()` → Average price of all orders

---

### ⭐ Bonus

- `Customer.most_aficionado(coffee)` → Class method returning the customer who spent the most on a given coffee

---

## ✅ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/coffee-shop-oop.git
cd coffee-shop-oop
