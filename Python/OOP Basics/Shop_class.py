# Create a Shop class with methods to add and list products

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product, price):
        self.products[product] = price
        print(f"Added {product} to {self.name}")

    def list_products(self):
        print(f"\nProducts in {self.name}:")

        for product, price in self.products.items():
            print(f"{product} - ₹{price}")


# Create objects
shop1 = Shop("SuperMart")
shop2 = Shop("TechStore")


# Add products to Shop 1
shop1.add_product("Milk", 50)
shop1.add_product("Bread", 30)
shop1.add_product("Eggs", 70)


# Add products to Shop 2
shop2.add_product("Keyboard", 1500)
shop2.add_product("Mouse", 800)
shop2.add_product("Headphones", 2500)


# List products
shop1.list_products()
shop2.list_products()