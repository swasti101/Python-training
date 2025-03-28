class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        tax = self.salary * 0.10  
        pf = self.salary * 0.12   
        return self.salary - (tax + pf)

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        tax = self.salary * 0.10
        pf = self.salary * 0.12
        return self.salary - (tax + pf)

class Contractor(Employee):
    def calculate_salary(self):
        tax = self.salary * 0.10  
        return self.salary - tax

# Testing
emp1 = FullTimeEmployee("Swasti", 101, 50000)
emp2 = PartTimeEmployee("Srajna", 102, 25000)
emp3 = Contractor("Sam", 103, 30000)

print(f"Name: {emp1.name}, Full time salary after deductions: {emp1.calculate_salary()}")
print(f"Name: {emp2.name}, Part-Time Salary after deductions: {emp2.calculate_salary()}")
print(f"Name: {emp3.name}, Contractor Salary after deductions: {emp3.calculate_salary()}")
