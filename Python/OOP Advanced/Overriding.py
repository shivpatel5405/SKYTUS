# Implement method overriding in a base and derived class.

# Base class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def show_role(self):
        print(f"{self.name} is a General Employee.")

    def calculate_salary(self):
        return self.base_salary


# Derived class inheriting from Employee
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def show_role(self):
        print(f"{self.name} is a Team Manager.")

    def calculate_salary(self):
        return self.base_salary + self.bonus


# Create objects of Base and Derived class
emp = Employee("Rahul", 50000)
mgr = Manager("Priya", 80000, 20000)


# Demonstrate Method Overriding
print("--- Base Class (Employee) ---")
emp.show_role()
print(f"Salary: {emp.calculate_salary()}")

print("\n--- Derived Class (Manager with Overridden Methods) ---")
mgr.show_role()
print(f"Salary: {mgr.calculate_salary()} (Includes {mgr.bonus} bonus)")
