from student_data import add_student, search_student, delete_student

def main():
    while True:
        print("\n📚 Student Records System 📚")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")
            add_student(name, age, grade)

        elif choice == "2":
            name = input("Enter Student Name to Search: ")
            student = search_student(name)
            if student:
                print(f"Student Found: {student}")
            else:
                print(f"Student {name} not found!")

        elif choice == "3":
            name = input("Enter Student Name to Delete: ")
            delete_student(name)

        elif choice == "4":
            print("Exiting!")
            break

        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    main()
