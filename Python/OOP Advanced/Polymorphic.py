# Create a polymorphic function that works with different shapes.

# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.name = "Rectangle"
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width


# Circle class
class Circle:
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def find_area(self):
        return 3.14159 * (self.radius ** 2)


# Triangle class
class Triangle:
    def __init__(self, base, height):
        self.name = "Triangle"
        self.base = base
        self.height = height

    def find_area(self):
        return 0.5 * self.base * self.height


# Polymorphic function 
def print_shape_details(shape):
    print(f"Shape: {shape.name}")
    print(f"Calculated Area: {shape.find_area():.2f}","\n")


# Create shape objects
rect = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(8, 4)

# Call the polymorphic function with different shapes
print("--- Demonstrating Polymorphic Function ---\n")
shapes = [rect, circle, triangle]

for s in shapes:
    print_shape_details(s)