# Strings and String Handling 

# Task 1: Take a string input and print its length.
print("--- Task 1: Take a string input and print its length ---")
string = input("Enter a string: ")
print(f"The length of the string is: {len(string)}" ,"\n")

# Task 2: Convert a sentence into lowercase
print("--- Task 2: Convert a sentence into lowercase ---")
sentence = input("Enter a sentence: ")
modified_sentence = sentence.lower()
print(f"The sentence in lowercase is: {modified_sentence}" ,"\n")

# Task 3: Replace spaces with underscores in a string
print("--- Task 3: Replace spaces with underscores in a string ---")
string = input("Enter a string with spaces: ")
new_string = string.replace(" ", "_")
print(f"The string with underscores is: {new_string}" ,"\n")


# Task 4: Extract the first character and the last character of a string
print("--- Task 4: Extract the first character and the last character of a string ---")
string = input("Enter a string: ")
first_character = string[0]
last_character = string[-1]
print(f"The first character is: {first_character} and The last character is: {last_character}" ,"\n")

      
# Task 5: Reverse a string using slicing
print("--- Task 5: Reverse a string using slicing ---")
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"The reversed string is: {reversed_string}" ,"\n")


# Task 6: Count how many times a letter appears in a string
print("--- Task 6: Count how many times a letter appears in a string ---")
string = input("Enter a string: ")
letter = input("Enter a letter to count: ")
count = string.count(letter)
print(f"The letter '{letter}' appears {count} times in the string." ,"\n")


# Task 7: Check if a word is present in a sentence
print("--- Task 7: Check if a word is present in a sentence ---")
sentence = input("Enter a sentence: ")
word = input("Enter a word to check: ")
if word in sentence:
    print(f"The word '{word}' is present in the sentence." ,"\n")
else:
    print(f"The word '{word}' is not present in the sentence." ,"\n")


# Task 8: Take name and age and print a using f-string formatting
print("--- Task 8: Take name and age and print using f-string formatting ---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old." ,"\n")


# Task 9: Remove the extra spaces from start and end of a string
print("--- Task 9: Remove the extra spaces from start and end of a string ---")
string = input("Enter a string with extra spaces: ")
new_string = string.strip()
print(f"The string without extra spaces is: {new_string}" ,"\n")


#Task 10: Join a list of words into a single string with - between them
print("--- Task 10: Join a list of words into a single string with - between them ---")
words = input("Enter a list of words separated by spaces: ").split()
new_string = "-".join(words)
print(f"The joined string is: {new_string}" ,"\n")  
