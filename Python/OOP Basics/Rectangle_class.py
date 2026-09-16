# Create a Rectangle class with a method to find area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * (self.length + self.width)

    def display_details(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.find_area()}")
        print(f"Perimeter: {self.find_perimeter()}")


# Create objects
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7.5, 3.2)

# Display rectangle 1 information
print("--- Rectangle 1 Details ---")
rect1.display_details()

print()

# Display rectangle 2 information
print("--- Rectangle 2 Details ---")
rect2.display_details()
