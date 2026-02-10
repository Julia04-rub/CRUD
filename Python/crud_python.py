employees = []

def create_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee's name: ")
    department = input("Enter employee department: ")
    position = input("Enter employee's position: ")
    salary = input("Enter employee's salary: ")

    employee = {
        "ID": employee_id,
        "Name": name,
        "Department": department,
        "Position": position,
        "Salary": salary
    }

    employees.append(employee)
    print(" Employee added successfully!")


def read_employee():
    if not employees:
        print(" No employees found.")
        return

    print(" Employee list:")
    for emp in employees:
        print(emp)
    print()


def search_employee():
    emp_id = input("Enter the employee ID you want to search: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            print(" Employee found:", emp)
            return

    print(" Employee not found.")


def update_employee():
    emp_id = input("Enter employee ID to update: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            print("Current Data:", emp)

            emp["Name"] = input("Enter new name: ")
            emp["Department"] = input("Enter new department: ")
            emp["Position"] = input("Enter new position: ")
            emp["Salary"] = input("Enter new salary: ")

            print("Employee updated successfully!")
            return

    print(" Employee not found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in employees:
        if emp["ID"] == emp_id:
            employees.remove(emp)
            print(" Employee deleted successfully!")
            return

    print(" Employee not found.")

def menu():
    while True:
        print("====== COMPANY EMPLOYEE SYSTEM ======")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employee()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")


menu()
