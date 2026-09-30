# Reports Module

from .database import get_products


def inventory_report():
    print("\n--- Inventory Report ---")

    products = get_products()

    if not products:
        print("No products available.")
        return

    total_products = len(products)
    total_quantity = 0
    total_value = 0

    for product in products:
        quantity = product[3]
        price = product[4]

        total_quantity += quantity
        total_value += quantity * price

    print("Total Different Products:", total_products)
    print("Total Quantity:", total_quantity)
    print("Total Inventory Value: ₹", total_value)