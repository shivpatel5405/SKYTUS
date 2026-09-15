# Write a program to demonstrate multiple exception blocks

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2

    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
