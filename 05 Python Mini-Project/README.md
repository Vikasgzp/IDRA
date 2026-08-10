# 🛒 Shopping Cart Management System

A menu-driven Shopping Cart Management System built using Python and Object-Oriented Programming (OOP).

This project demonstrates the Python concepts learned throughout Week 1, including variables, conditional statements, loops, functions, data structures, exception handling, file handling, and OOP.

## 🚀 Features

- View all available products
- Search products by name or category
- Add products to cart
- View shopping cart
- Remove products from cart
- Update product quantities
- Automatic stock management
- Automatic discount calculation
- Checkout system
- Generate bill in a TXT file
- Store product information in CSV
- Handle invalid user input gracefully

## 🧠 Python Concepts Used

### Object-Oriented Programming

- Classes
- Objects
- Constructors
- Instance variables
- Methods

### Data Structures

- Lists
- Dictionaries
- Tuples
- Sets

### Other Concepts

- Variables
- Conditional statements
- Loops
- Functions
- Exception handling
- CSV file handling
- TXT file handling
- Date and time

## 📁 Project Structure

```text
shopping-cart-system/
│
├── shopping_cart.py
├── products.csv
├── bill.txt
└── README.md


```

products.csv and bill.txt are automatically created by the program when required.

💰 Discount System

The application automatically applies discounts during checkout:
| Cart Total | Discount |
| --------------- | -------- |
| Below ₹5,000 | 0% |
| ₹5,000 - ₹9,999 | 5% |
| ₹10,000+ | 10% |

🧾 Bill Generation

After a successful checkout, the application generates a bill.txt file containing:

Purchase date and time
Products purchased
Quantities
Subtotal
Discount
Final amount

| ID  | Product    | Category    | Price   |
| --- | ---------- | ----------- | ------- |
| 101 | Laptop     | Electronics | ₹55,000 |
| 102 | Mouse      | Electronics | ₹800    |
| 103 | Keyboard   | Electronics | ₹1,500  |
| 104 | Headphones | Electronics | ₹2,000  |
| 105 | T-Shirt    | Clothing    | ₹700    |
| 106 | Jeans      | Clothing    | ₹1,800  |
| 107 | Backpack   | Accessories | ₹1,200  |
| 108 | Watch      | Accessories | ₹2,500  |

👨‍💻 Author

Vikas Kushwaha
