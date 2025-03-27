import csv
import os

FILE_NAME = "students.csv"

# file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Grade"])  # Header row

#Function to Add a Student
def add_student(name, age, grade):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])
    print(f"Student {name} added successfully!")

#Function to Search for a Student
def search_student(name):
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                return row
    return None

#Function to Delete a Student
def delete_student(name):
    students = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader) 
        for row in reader:
            if row[0].lower() != name.lower():
                students.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write the header back
            writer.writerows(students)  # Write remaining students
        print(f"Student {name} deleted successfully!")
    else:
        print(f"Student {name} not found!")
