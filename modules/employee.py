
employees = []


def add_employee():
    print("\n--- Add Employee ---")

    employee_id = input("Enter employee ID: ").strip()
    name = input("Enter employee name: ").strip()
    role = input("Enter employee role: ").strip()

    if not employee_id or not name or not role:
        print("All fields are required.")
        return

    employee = {
        "id": employee_id,
        "name": name,
        "role": role
    }

    employees.append(employee)

    print("Employee added successfully!")


def view_employees():
    print("\n--- Employee List ---")

    if not employees:
        print("No employees available.")
        return

    for employee in employees:
        print("------------------------")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Role:", employee["role"])