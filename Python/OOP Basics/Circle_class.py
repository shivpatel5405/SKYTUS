# Create a Circle Class to find it's area and circumference

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def find_area(self):
        return self.PI * (self.radius ** 2)

    def find_circumference(self):
        return 2 * self.PI * self.radius

    def display_details(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.find_area():.2f}")
        print(f"Circumference: {self.find_circumference():.2f}")


# Create objects
circle1 = Circle(5)
circle2 = Circle(7.5)

# Display circle 1 information
print("--- Circle 1 Details ---")
circle1.display_details()

print()

# Display circle 2 information
print("--- Circle 2 Details ---")
circle2.display_details()