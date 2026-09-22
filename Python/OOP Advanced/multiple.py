# Demonstrate multiple inheritance with two parent classes

# First parent class
class Camera:
    def take_photo(self):
        print("Camera: Taking a photo.")


# Second parent class
class Phone:
    def make_call(self, number):
        print(f"Phone: Calling {number}...")


# Child class inheriting from both
class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("SmartPhone: Browsing the internet.")


# Create an object of the child class
my_phone = SmartPhone()

# Access methods inherited from both parent 
print("--- Multiple Inheritance in Action ---")
my_phone.make_call("9876543210")   
my_phone.take_photo()               
my_phone.browse_internet()         
