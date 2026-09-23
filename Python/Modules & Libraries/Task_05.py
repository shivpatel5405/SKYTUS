# Use math module to find factorial of a number.
import math

# Taking user input
num = int(input("Enter a number: "))

if num >= 0:
    result = math.factorial(num)
    print(f"The factorial of {num} is: {result}")
else:
    print("Factorial is not defined for negative numbers.")
    