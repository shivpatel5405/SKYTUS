#Compare two numbers and print the largest one 

num1=int(input("Enter the number-1 : "))
num2=int(input("Enter the number-2 : "))

if num1>num2:
    print(num1, "is the greater number")
elif num2>num1:
    print(num2, "is the greater number")
else:
    print("Both numbers are equal")
