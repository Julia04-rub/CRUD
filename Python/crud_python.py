import sqlite3


conn = sqlite3.connect("employees.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL
)
''')
conn.commit()


def add_employee():
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
                   (name, position, salary))
    conn.commit()
    print("Employee {name} added successfully!")


def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    if not employees:
        print("No employees found.")
        return
    
    print("--- Employees List ---")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}")
    print()


def update_employee():
    emp_id = input("Enter employee ID to update: ")
    
    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    employee = cursor.fetchone()
    
    if not employee:
        print("Employee not found.")
        return
    
    name = input("Enter new name ({employee[1]}): ") or employee[1]
    position = input("Enter new position ({employee[2]}): ") or employee[2]
    salary_input = input("Enter new salary ({employee[3]}): ")
    salary = float(salary_input) if salary_input else employee[3]
    
    cursor.execute("UPDATE employees SET name=?, position=?, salary=? WHERE id=?",
                   (name, position, salary, emp_id))
    conn.commit()
    print(f"Employee ID {emp_id} updated successfully!")


def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    
    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    employee = cursor.fetchone()
    
    if not employee:
        print("Employee not found.")
        return
    
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    print("Employee ID {emp_id} deleted successfully!")


def main():
    while True:
        print(" Employee Management System ")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
    conn.close()
