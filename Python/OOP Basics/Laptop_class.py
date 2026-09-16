# Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount
        print(f"Applied {discount_percentage}% discount. Saved: {discount_amount}")
        print(f"After Discount The Price is: {self.price}")

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")


# Create objects
laptop1 = Laptop("Apple", "MacBook Pro", 120000)
laptop2 = Laptop("Asus", "TUF GAMING ", 95000)

# Display laptop 1 information
print("--- Laptop 1 Details ---")
laptop1.display_details()
print("\nApplying discount to Laptop 1:")
laptop1.apply_discount(10)

# Display laptop 2 information
print("\n--- Laptop 2 Details ---")
laptop2.display_details()
print("\nApplying discount to Laptop 2:")
laptop2.apply_discount(15)