from fetch_data import read_csv
from process_data import calculate_total_marks
from report_data import write_csv

# Step 1: Read CSV
students = read_csv("/Users/consultadd/Desktop/python training/File Handling/file handling with modules/students.csv")


# Step 2: Process Data (Calculate Total Marks)
students = calculate_total_marks(students)

# Step 3: Save Updated Data
write_csv("/Users/consultadd/Desktop/python training/File Handling/file handling with modules/output.csv", students)

print("Processing completed! Updated data saved to output.csv.")
