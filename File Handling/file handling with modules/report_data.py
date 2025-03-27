import csv

def write_csv(file_name, students):
    fieldnames = ["StudentID", "Name", "Math", "Science", "English", "Total"]
    
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
