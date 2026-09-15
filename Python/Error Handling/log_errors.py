# Write a program to log errors to a file instead of printing them

import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2
    print("Result:", result)

except ValueError:
    logging.error("Invalid input. Please enter numbers.")

except ZeroDivisionError:
    logging.error("Cannot divide by zero.")