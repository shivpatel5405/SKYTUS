# Write a program to shuffle a list using a random module

import random

numbers = [1, 2, 3, 4, 5, 6]

print("Original list:", numbers)

random.shuffle(numbers)  #  using random.shuffle()

print("Shuffled list:", numbers)