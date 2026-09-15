# Write a program to handle invalid integer input
while True:
    try:
        number = int(input("Enter an integer: "))
        print(f"You entered: {number}")
        break

    except ValueError:
        print("Invalid input! Please enter an integer.")