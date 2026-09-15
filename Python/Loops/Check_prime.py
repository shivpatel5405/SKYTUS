# Check if the number is prime or not 
number = int(input("\n\nEnter the number: ")) 
if number < 1 : 
    print(f"{number} is not a Prime number") 
else: 
    is_prime = True 
for i in range(2, number): 
    if number % 2 == 0: 
        is_prime = False 
        break 

if is_prime: 
    print(f"{number} is prime number") 
else: 
    print(f"{number} is not a prime number")