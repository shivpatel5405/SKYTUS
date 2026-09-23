# Import multiple function from one module and use them

from maths import add, subtract, multiply


# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Use the imported functions
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))