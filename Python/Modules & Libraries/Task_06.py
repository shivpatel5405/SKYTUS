# Create a package shapes with modules for circle and rectangle.

from shapes import circle, rectangle

# Circle operations
print("--- Circle Operations ---")
radius = float(input("Enter radius of the circle: "))
print(f"Area of Circle: {circle.area(radius):.2f}")
print(f"Perimeter of Circle: {circle.perimeter(radius):.2f}")

# Rectangle operations
print("\n--- Rectangle Operations ---")
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
print(f"Area of Rectangle: {rectangle.area(length, width):.2f}")
print(f"Perimeter of Rectangle: {rectangle.perimeter(length, width):.2f}")