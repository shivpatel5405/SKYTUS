# Functin to check if a word is palindrome or not
def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")

    # Check if the word is equal to its reverse
    return word == word[::-1]

string = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")