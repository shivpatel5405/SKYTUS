# Create a custom math module and import it in another file.

import maths

print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (+, -, *, / or 1, 2, 3, 4): ")

if choice in ('1', '2', '3', '4', '+', '-', '*', '/'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice in ('1', '+'):
        print(f"Result: {maths.add(num1, num2)}")
    elif choice in ('2', '-'):
        print(f"Result: {maths.subtract(num1, num2)}")
    elif choice in ('3', '*'):
        print(f"Result: {maths.multiply(num1, num2)}")
    elif choice in ('4', '/'):
        print(f"Result: {maths.divide(num1, num2)}")
else:
    print("Invalid choice! Please select a valid operation.")
