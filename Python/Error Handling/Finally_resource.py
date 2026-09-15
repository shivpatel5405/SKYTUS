# Write a program to use finally for resource clean-up

try:
    print("Opening resource...")
    
    number = int(input("Enter a number: "))
    result = 100 / number
    
    print(f"Result: {result}")

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Closing resource...")
    print("Cleanup completed.")