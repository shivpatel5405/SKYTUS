# Display the multiplication table for a given number 
number = int(input("\nEnter a number : ")) 
for i in range(1,11): 
    print(f"{number} * {i} = {number * i}")