def calculate_total_marks(students):
    """ Adds a Total column by summing Math, Science, and English marks """
    for student in students:
        student["Total"] = int(student["Math"]) + int(student["Science"]) + int(student["English"])
    return students
