import csv

def read_csv(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
