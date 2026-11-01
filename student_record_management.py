
import csv
import json
import os

FILE_NAME = "students.json"

# Load student records
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []

# Save student records
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    try:
        student_id = input("Enter Student ID: ")

        if any(s["id"] == student_id for s in students):
            print("Student ID already exists!")
            return

        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks!")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }

        students.append(student)
        save_students(students)
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numbers!")

# View students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    for s in students:
        print("\n----------------------")
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Course:", s["course"])
        print("Marks:", s["marks"])

# Search student
def search_student(students):
    student_id = input("Enter Student ID: ")

    for s in students:
        if s["id"] == student_id:
            print("Student Found:", s)
            return

    print("Student not found!")

# Update student
def update_student(students):
    student_id = input("Enter Student ID: ")

    for s in students:
        if s["id"] == student_id:
            s["name"] = input("Enter New Name: ")
            s["course"] = input("Enter New Course: ")

            try:
                s["marks"] = float(input("Enter New Marks: "))
                if not 0 <= s["marks"] <= 100:
                    print("Invalid marks!")
                    return
            except ValueError:
                print("Invalid marks!")
                return

            save_students(students)
            print("Record updated successfully!")
            return

    print("Student not found!")

# Delete student
def delete_student(students):
    student_id = input("Enter Student ID: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")

# Export records to CSV
def export_csv(students):
    with open("students.csv", "w", newline="") as file:
        fields = ["id", "name", "age", "course", "marks"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)

    print("CSV file created successfully!")

# Main program
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT RECORD MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                export_csv(students)
            elif choice == "7":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
