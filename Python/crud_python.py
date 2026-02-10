import json
import os

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")

    
    for student in students:
        if student["id"] == student_id:
            print("❌ Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(new_student)
    save_students(students)

    print("✅ Student added successfully!")


def view_students():
    students = load_students()

    if len(students) == 0:
        print("📌 No students found!")
        return

    print("\n--- STUDENT LIST ---")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")


def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("\nLeave blank if you don’t want to change a field.")

            new_name = input(f"Enter new name ({student['name']}): ")
            new_age = input(f"Enter new age ({student['age']}): ")
            new_course = input(f"Enter new course ({student['course']}): ")

            if new_name != "":
                student["name"] = new_name
            if new_age != "":
                student["age"] = new_age
            if new_course != "":
                student["course"] = new_course

            save_students(students)
            print("✅ Student updated successfully!")
            return

    print("❌ Student not found!")


def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("✅ Student deleted successfully!")
            return

    print("❌ Student not found!")


def search_student():
    students = load_students()
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\n--- STUDENT FOUND ---")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            return

    print("❌ Student not found!")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again!")


main()
