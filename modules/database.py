import sqlite3

DATABASE_NAME = "inventory.db"


def connect_database():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_product(name, category, quantity, price):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products (name, category, quantity, price)
        VALUES (?, ?, ?, ?)
    """, (name, category, quantity, price))

    connection.commit()
    connection.close()


def get_products():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    connection.close()

    return products