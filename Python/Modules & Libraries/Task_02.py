# Import custom string module
import string_ops

text = input("Enter a string: ")

# Display results
print("\n===== String Operations =====")

print("Original String:", text)
print("Reverse:", string_ops.reverse_string(text))
print("Number of Characters:", string_ops.count_characters(text))
print("Uppercase:", string_ops.convert_uppercase(text))
print("Lowercase:", string_ops.convert_lowercase(text))
print("Number of Words:", string_ops.count_words(text))
