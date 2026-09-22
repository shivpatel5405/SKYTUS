# Create a base class Animal and Subclasses Dog and Cat

# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating food.")


# Subclass Dog inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking: Woof! Woof!")


# Subclass Cat inheriting from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing: Meow! Meow!")


# Create objects
dog1 = Dog("Rocky", 3,)
cat1 = Cat("Luna", 2,)


# Display Dog details and actions
print("--- Dog Details ---")
print(f"Name: {dog1.name}, Age: {dog1.age} years")
dog1.eat()   
dog1.bark() 

# Display Cat details and actions
print("\n--- Cat Details ---")
print(f"Name: {cat1.name}, Age: {cat1.age} years")
cat1.eat()   
cat1.meow()  
