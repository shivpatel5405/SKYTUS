# Create a Car class with attributes like brand, model and speed
# and methods to accelerate/brake

class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Car accelerated. Speed:", self.speed)

    def brake(self):
        self.speed -= 20

        if self.speed < 0:
            self.speed = 0

        print("Car slowed down. Speed:", self.speed)


# Create objects
car1 = Car("Toyota", "Fortuner", 50)
car2 = Car("BMW", "M-5", 70)


# Display car 1 information
print(f"The brand of the car is: {car1.brand} ; "
      f"The model of the car is: {car1.model} ; "
      f"The base speed of the car is: {car1.speed}")

car1.accelerate()
car1.brake()


# Display car 2 information
print(f"The brand of the car is: {car2.brand} ; "
      f"The model of the car is: {car2.model} ; "
      f"The base speed of the car is: {car2.speed}")

car2.accelerate()
car2.brake()