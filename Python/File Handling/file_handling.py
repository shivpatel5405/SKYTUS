# Task 1: Write a Program read a file and display its contents
with open("file.txt","r") as file:
    content = file.read()
    print(f"The Content of the file is : {content}" , "\n")


# Task 2: Write a Program to count the number of lines in the file 
with open("file.txt","r") as file:
    content = file.readlines()
    print(f"The number of lines in the file are : {len(content)}" , "\n")


# Task 3: Write a Program to count how many times each word appears in file
with open("file.txt", "r") as file:
    content = file.read()

words = content.split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(f"Word frequency in the file:{ word_freq}", "\n")


# Task 4: Write a Program to write 5 user-entered sentences to a file
with open("file2.txt", "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i + 1}: ")
        file.write(sentence + "\n")

print(f"5 sentences have been written to the file.", "\n")


# Task 5: Write a Program to  append a list of strings to an existing file
strings = ["Python is easy", "Django is framework", "MySQL is used for database", "JavaScript is a scripting language"]

with open("file3.txt", "a") as file:
    for string in strings:
        file.write(string +"\n")

print(f"Strings have been appended to the file.", "\n")


# Task 6: Write a Program to print lines containing a specific word
word = input("Enter the word to search: ")

with open("file.txt", "r") as file:
    for line in file:
        if word in line:
            print(line, end="")


# Task 7:Write a Program to replace a specific word in a file

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

with open("file2.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("file2.txt", "w") as file:
    file.write(content)

print(f"Word replaced successfully.", "\n")


# Task 8: Write a Program to merge two files into a third file

with open("file.txt", "r") as file1:
    content1 = file1.read()

with open("file2.txt", "r") as file2:
    content2 = file2.read()

with open("file3.txt", "w") as file3:
    file3.write(content1)
    file3.write("\n")
    file3.write(content2)

print(f"Files merged successfully.", "\n")


# Task 9: Read a CSV file and display its contents

import csv

with open("Students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)



# Task 10:Write a Program to Create a backup of a file

with open("file.txt", "r") as source:
    content = source.read()

with open("backup.txt", "w") as backup:
    backup.write(content)

print(f"Backup created successfully.","\n")