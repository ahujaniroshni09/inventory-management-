# Billing and Sales Module

from .database import connect_database


def sell_product():
    print("\n--- Sell Product ---")

    product_id_text = input("Enter product ID: ").strip()
    quantity_text = input("Enter quantity to sell: ").strip()

    if not product_id_text.isdigit():
        print("Product ID must be a number.")
        return

    if not quantity_text.isdigit():
        print("Quantity must be a whole number.")
        return

    product_id = int(product_id_text)
    quantity = int(quantity_text)

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name, quantity, price FROM products WHERE id = ?",
        (product_id,)
    )

    product = cursor.fetchone()

    if product is None:
        print("Product not found.")
        connection.close()
        return

    name, available_quantity, price = product

    if quantity > available_quantity:
        print("Not enough stock available.")
        connection.close()
        return

    total = quantity * price

    new_quantity = available_quantity - quantity

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE id = ?",
        (new_quantity, product_id)
    )

    connection.commit()
    connection.close()

    print("\nSale completed successfully!")
    print("Product:", name)
    print("Quantity:", quantity)
    print("Total Amount: ₹", total)