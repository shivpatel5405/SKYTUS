# Generate the First N fibonacci numbers 
number = int(input("\nEnter the number of terms: ")) 
a = 0
b = 1 
print(f"The Fibonacci series of {number} terms is:") 
for i in range(number): 
    print(a, end=" ") 
    c = a + b 
    a = b 
    b = c