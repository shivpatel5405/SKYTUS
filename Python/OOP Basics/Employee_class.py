# Create a Employee class that displays salary details

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def calculate_annual_salary(self):
        return self.salary * 12

    def display_salary_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: {self.salary}")
        print(f"Annual Salary: {self.calculate_annual_salary()}")


# Create objects
emp1 = Employee("Cristino ", "EMP101", "IT", 60000)
emp2 = Employee("Alexis Puttiles", "EMP102", "Backend", 75000)

# Display employee 1 salary details
print("--- Employee 1 Salary Details ---")
emp1.display_salary_details()

print()

# Display employee 2 salary details
print("--- Employee 2 Salary Details ---")
emp2.display_salary_details()
