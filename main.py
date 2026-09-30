# ==========================================
# INVENTORY MANAGEMENT SYSTEM
# ==========================================

from modules.database import create_tables
from modules.auth import login
from modules.inventory import add_new_product, view_products
from modules.billing import sell_product
from modules.employee import add_employee, view_employees
from modules.reports import inventory_report


def main():
    create_tables()

    if not login():
        return

    while True:
        print("\n==============================")
        print("   INVENTORY MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Sell Product")
        print("4. Add Employee")
        print("5. View Employees")
        print("6. Inventory Report")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_new_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            sell_product()

        elif choice == "4":
            add_employee()

        elif choice == "5":
            view_employees()

        elif choice == "6":
            inventory_report()

        elif choice == "7":
            print("Thank you for using the Inventory Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()