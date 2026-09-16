# Create a Student class with a method to calculate average marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average():.2f}")


# Create objects
student1 = Student("Alice", [])
student2 = Student("Bob", [70, 65, 80, 75, 85])

# Display student 1 information
print("--- Student 1 Details ---")
student1.display_details()

print()

# Display student 2 information
print("--- Student 2 Details ---")
student2.display_details()
