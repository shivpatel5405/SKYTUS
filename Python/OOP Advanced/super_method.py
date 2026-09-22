# Demonstrate the use of super() in inheritance.

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived class inheriting from Person
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        super().display_info()                  # parent class display_info method
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


# Create an object of the derived class
emp = Employee("Rohan", 25, "EMP101", 55000)

# Display details
print("--- Employee Details ---")
emp.display_info()