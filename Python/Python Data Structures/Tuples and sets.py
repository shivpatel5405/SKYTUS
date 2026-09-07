# Task 1 : Create a tuple with 5 numbers
numbers = (1, 2, 3, 4, 5)
print(f"Tuple with 5 numbers: {numbers}", "\n")

# Task 2 : Access the Third element of the tuple
print(f"Third element of the tuple: {numbers[2]}", "\n")

# Task 3 : Unpack the tuple into seperate variables
a, b, c, d, e = numbers
print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}", "\n") 

# Task 4 : Create a set of 5 unique numbers
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(f"Set of 5 unique numbers: {numbers}", "\n")

# Task 5 : Add a new fruit to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("date")
print(f"Set of fruits after adding a new fruit: {fruits}", "\n")

# Task 6 : Remove a fruit from the set
fruits.remove("banana")
print(f"Set of fruits after removing a fruit: {fruits}", "\n")

# Task 7 : Remove an element from the set 
'''fruits.remove("kiwi")  --> This will raise a KeyError if "kiwi" is not in the set'''
fruits.discard("apple")  # Using discard to avoid KeyError if the element doesn't exist
print(f"Set of fruits after discarding a fruit: {fruits}", "\n")

# Task 8 : find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}", "\n")

# Task 9 : find the intersection of two sets
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}", "\n")

# Task 10 : Check if one set is a subset of another
is_subset = set1.issubset(set2)
print(f"Is set1 a subset of set2 ? : {is_subset}", "\n")

# Task 11 : Convert a list with duplicate value into a set to remove duplicates
list = [1, 2, 2, 3, 4, 4, 5]
new_set = set(list)
print(f"Set after converting list with duplicates: {new_set}", "\n")