# write a program that validates an email format and raises an exception for invalid ones

class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format.")

    print("Valid email.")

except InvalidEmailError as e:
    print("Error:", e)