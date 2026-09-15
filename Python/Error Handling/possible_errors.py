# Write a program that takes two numbers and handles all possible errors

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2

    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print(f"Some other error occurred: {e}")