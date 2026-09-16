# Create a Flight Class with seat booking functionality

class Flight:
    def __init__(self, flight_number, destination, seats):
        self.flight_number = flight_number
        self.destination = destination
        self.seats = seats

    def book_seat(self, num):
        if num <= self.seats:
            self.seats -= num
            print(f"{num} seat(s) booked successfully. Remaining seats: {self.seats}")
        else:
            print("Not enough seats available!")


# Create object
flight1 = Flight("AI-202", "Mumbai", 50)

# Display flight information
print(f"Flight: {flight1.flight_number}, Destination: {flight1.destination}, Available Seats: {flight1.seats}")

# Book seats
flight1.book_seat(10)
flight1.book_seat(45)

