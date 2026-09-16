# Create a Books class to store title , author , price and display details

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


# Create objects
book1 = Book("The Alchemist", "Paulo Coelho", 350)
book2 = Book("Atomic Habits", "James Clear", 450)

# Display book 1 information
print("--- Book 1 Details ---")
book1.display_details()

# Display book 2 information
print("\n--- Book 2 Details ---")
book2.display_details()