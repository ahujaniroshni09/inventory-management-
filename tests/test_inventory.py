from modules.database import create_tables, add_product, get_products


def test_add_product():
    create_tables()

    add_product("Test Pen", "Stationery", 10, 20)

    products = get_products()

    assert len(products) > 0

    print("Test passed: Product was added successfully.")


if __name__ == "__main__":
    test_add_product()