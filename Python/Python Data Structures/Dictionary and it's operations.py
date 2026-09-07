# Task 1: create a dictionary storing student name and marks
student_marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 78
}
print(f"Dictionary of student marks: {student_marks}", "\n")

# Task 2: Add a new key-value pair to an existing dictionary
student_marks["Eve"] = 88
print(f"Dictionary after adding a new student: {student_marks}", "\n")

# Task 3: Delete a key-value pair from the dictionary
del student_marks["Bob"]
print(f"Dictionary after deleting a student: {student_marks}", "\n")

# Task 4: Merge two dictionaries into one
new_added_marks = {
    "Charlie": 90,
    "David": 95
}
merged_marks = {**student_marks, **new_added_marks}
print(f"Merged dictionary: {merged_marks}", "\n")

# Task 5: Check if a key exists in the dictionary
check = "Alice"
if check in merged_marks:
    print(f"{check} exists in the dictionary with marks: {merged_marks[check]}", "\n")

# Task 6: Count word frequency in a string using dictionary
String = "Python is a great programming language. Python is widely used in data science."
words = String.split()
word_freq = {}
for i in words:
    word_freq[i] = word_freq.get(i, 0) + 1
print(f"Word frequency in the string: {word_freq}", "\n")

# Task 7: find the key with the maximum value in a dictionary
max_key = max(merged_marks, key=merged_marks.get)
print(f"Student with maximum marks is : {max_key} and his max marks is : {merged_marks[max_key]}", "\n") 

# Task 8: Reverse keys and values in a dictionary
reversed_dict = {value: key for key, value in merged_marks.items()}
print(f"Reversed dictionary: {reversed_dict}", "\n")

# Task 9: update the value for a specific key
merged_marks["Alice"] = 95
print(f"Dictionary after updating Alice's marks: {merged_marks}", "\n")

# Task 10: Convert the list of  tuples into a dictionary
list_of_tuples = [("John", 85), ("Alice", 92), ("Bob", 78)]
dict_from_tuples = dict(list_of_tuples)
print(f"Dictionary from list of tuples: {dict_from_tuples}", "\n")
