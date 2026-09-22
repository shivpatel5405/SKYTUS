# Create a class hierarchy for Vehicle - Car - ElectricCar.

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.model} is starting.")

    def stop(self):
        print(f"{self.model}  has stopped.")


# Subclass Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def honk(self):
        print(f"{self.model} says: Beep! Beep!")


# Subclass ElectricCar inheriting from Car 
class ElectricCar(Car):
    def __init__(self, brand, model, seating_capacity, battery_capacity):
        super().__init__(brand, model, seating_capacity)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} is charging its {self.battery_capacity} kWh battery.")


# Create objects
car1 = Car("Toyota", "Fortuner", 7)
ev1 = ElectricCar("Tesla", "Model Y ", 5, 75)

# Display Car details and actions
print("--- Car Details ---")
print(f"Brand: {car1.brand}, Model: {car1.model}, Seats: {car1.seating_capacity}")
car1.start()
car1.honk()
car1.stop()

# Display ElectricCar details and actions
print("\n--- Electric Car Details ---")
print(f"Brand: {ev1.brand}, Model: {ev1.model}, Seats: {ev1.seating_capacity}, Battery: {ev1.battery_capacity} kWh")
ev1.start()
ev1.charge()
ev1.honk()
ev1.stop()