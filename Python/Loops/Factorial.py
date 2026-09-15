# Find Factorial of the number 
number = int(input("\nEnter a number : ")) 
result = 1 
for i in range(1, number + 1):
    result *= i 
print(f"The Factorial of {number} is {result}" )