# Write a program to handle division by zero error
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2

    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")