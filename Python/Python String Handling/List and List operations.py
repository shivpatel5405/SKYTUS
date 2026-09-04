# List and List operations/methods 

# Task 1: Create a list of your 5 favorite movies
print("--- Task 1: Create a list of your 5 favorite movies ---")
favorite_movies = ["KGF", "Fighter", "Toxic", "Spider-Man", "Avengers Endgame"]
print(f"The list of favorite movies is: {favorite_movies}" , "\n")

# Task 2: Add a new movie to the list
print("--- Task 2: Add a new movie to the list ---")
new_movie = input("Enter a new movie to add to the list: ")
favorite_movies.append(new_movie)
print(f"The updated list of favorite movies is: {favorite_movies}" , "\n")

# Task 3: Remove the first movie from the list
print("--- Task 3: Remove the first movie from the list ---")
favorite_movies.pop(0)
print(f"The updated list of favorite movies is: {favorite_movies}" , "\n")

# Task 4: Sort a list of numbers in ascending order
print("--- Task 4: Sort a list of numbers in ascending order ---")
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(f"The sorted list is: {numbers}" , "\n")

# Task 5: Reverse a list 
print("--- Task 5: Reverse a list ---")
numbers.reverse()
print(f"The reversed list is: {numbers}" , "\n")

# Task 6: Find the largest number in a list
print("--- Task 6: Find the largest number in a list ---")
largest_number = max(numbers)
print(f"The largest number in the list is: {largest_number}" , "\n")

# Task 7: Merge two lists into one
print("--- Task 7: Merge two lists into one ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(f"The merged list is: {merged_list}" , "\n")


# Task 8: Access the last element of a list without using the index number
print("--- Task 8: Access the last element of a list without using the index number ---")
list1 = [10, 20, 30, 40, 50]
last_element = list1[-1]
print(f"The last element of the list is: {last_element}" , "\n")


# Task 9: Create a nested list and access a specific inner element 

print("--- Task 9: Create a nested list and access a specific inner element ---")
nested_list = [[1, 2], [3, 4], [5, 6]]
inner_element = nested_list[1][0]
print(f"The specific inner element is: {inner_element}" , "\n")


# Task 10: Count how many times an element appears in a list

print("--- Task 10: Count how many times an element appears in a list ---")
numbers = [10, 20, 10, 30, 10, 40, 20]
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print(f"The element appears {count} times.","\n")
