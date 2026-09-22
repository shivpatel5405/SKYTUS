# Create a Teacher and Student class to show inheritance.

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Subclass: Teacher inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


# Subclass: Student inheriting from Person
class Student(Person):
    def __init__(self, name, age, standard):
        super().__init__(name, age)
        self.standard = standard

    def study(self):
        print(f"{self.name} is studying in Standard {self.standard}.")


# Create objects
teacher = Teacher("Mrs. Sharma", 35, "Mathematics")
student = Student("Aman", 15,10)

# Display Teacher details and actions
print("--- Teacher Details ---")
teacher.display_details()
print(f"Subject: {teacher.subject}")
teacher.teach()

# Display Student details and actions
print("\n--- Student Details ---")
student.display_details()
print(f"Standard: {student.standard}")
student.study()