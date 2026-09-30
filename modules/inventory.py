# Inventory Management Module

from .database import add_product, get_products


def add_new_product():
    print("\n--- Add Product ---")

    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()
    quantity_text = input("Enter quantity: ").strip()
    price_text = input("Enter price: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    if not category:
        print("Category cannot be empty.")
        return

    if not quantity_text.isdigit():
        print("Quantity must be a whole number.")
        return

    try:
        quantity = int(quantity_text)
        price = float(price_text)
    except ValueError:
        print("Price must be a valid number.")
        return

    if quantity < 0 or price < 0:
        print("Quantity and price cannot be negative.")
        return

    add_product(name, category, quantity, price)

    print("Product added successfully!")


def view_products():
    print("\n--- Inventory ---")

    products = get_products()

    if not products:
        print("No products available.")
        return

    print("ID | Name | Category | Quantity | Price")

    for product in products:
        print(
            product[0],
            "|",
            product[1],
            "|",
            product[2],
            "|",
            product[3],
            "| ₹",
            product[4]
        )