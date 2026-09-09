# Function to check if a number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1): # Check possible divisors up to the square root
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")