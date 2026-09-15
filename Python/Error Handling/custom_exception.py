# Write a program to create s custom exception for invalid age (<18)

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("You are eligible.")

except InvalidAgeError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter a valid integer.")