#Write a program to swap the values of two variable 

a = int(input("Enter the number-1 : "))
b = int(input("Enter the number-2 : "))

print(f"Before swapping : a = {a} , b = {b}")

temp = a
a = b
b = temp

print(f"After swapping: a = {a} , b = {b}") 
