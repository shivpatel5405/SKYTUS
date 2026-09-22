# Create a class with private attributes and getter/setter methods

class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for marks
    def get_marks(self):
        return self.__marks

    # Setter for marks
    def set_marks(self, marks):
        self.__marks = marks


# Create object
student = Student("Rahul", 85)

# Get values
print("Name:", student.get_name())
print("Marks:", student.get_marks())

# Set new values
student.set_name("Amit")
student.set_marks(90)

# Display updated values
print("\nAfter updating:")
print("Name:", student.get_name())
print("Marks:", student.get_marks())