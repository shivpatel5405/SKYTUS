# Use random module to generate 5 random integers.

import random

print("5 Random Integers (between 1 and 100):")

# Generate and display 5 random integers
for i in range(1, 6):
    number = random.randint(1, 100)
    print(f"Number {i}: {number}")