# Login and Authentication Module


USERNAME = "admin"
PASSWORD = "1234"


def login():
    print("\n==============================")
    print("   INVENTORY MANAGEMENT LOGIN")
    print("==============================")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin successful!")
        return True
    else:
        print("\nInvalid username or password.")
        return False