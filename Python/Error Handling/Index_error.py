# Write a program to handle IndexError when accessing a list
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index: "))
    print(f"Value: {numbers[index]}")

except IndexError:
    print("Error: Index is out of range.")

except ValueError:
    print("Error: Please enter a valid integer.")