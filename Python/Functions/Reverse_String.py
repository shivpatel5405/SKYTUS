# Function to reverse a string
def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")