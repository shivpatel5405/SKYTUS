# use os module to list the files in a directory 

import os

path = input("Enter directory path: ")

items = os.listdir(path)

print("\nFiles and folders in the directory:")

for i in items:
    print(i)