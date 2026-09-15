# Write a program to open a file and handle the "File Not Found" error

try:
    file = open("file.txt", "r")
    
    content = file.read()
    print(content)
    
    file.close()

except FileNotFoundError:
    print("Error: File not found.")