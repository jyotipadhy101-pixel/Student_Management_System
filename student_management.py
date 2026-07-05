import csv

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, age, course])

print("Student added successfully!")

add_student()

import csv

def view_students():
    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

view_students()

import csv

def search_student():
    search_roll = input("Enter Roll Number to Search: ")

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == search_roll:
                print("Student Found:")
                print(row)
                return

        print("Student not found!")

search_student()

import csv

def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    students = []

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == roll_no:
                print("Student Found!")

                row[1] = input("Enter New Name: ")
                row[2] = input("Enter New Age: ")
                row[3] = input("Enter New Course: ")

            students.append(row)

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("Student Updated Successfully!")

update_student()

import csv

def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    students = []

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] != roll_no:
                students.append(row)

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("Student Deleted Successfully!")

delete_student()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")