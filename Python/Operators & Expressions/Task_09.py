# Write a program that uses and & or operators to check multiple conditions
num = int(input("Enter a number: "))
if num > 0 and num < 10:
    print("The number is between 0 and 10")
elif num >= 10 or num <= 0:
    print("The number is either greater than or equal to 10 or less than or equal to 0")