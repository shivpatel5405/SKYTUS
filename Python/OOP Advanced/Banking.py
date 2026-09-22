# Create a Bank system with SavingsAccount and CurrentAccount classes.

# Base class
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.holder} deposited: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.holder}: Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{self.holder} withdrew: {amount}. Balance: {self.balance}")


# Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, holder, balance, rate):
        super().__init__(holder, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * (self.rate / 100)
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")


# Current Account
class CurrentAccount(BankAccount):
    def __init__(self, holder, balance, limit):
        super().__init__(holder, balance)
        self.limit = limit

    # Method overriding
    def withdraw(self, amount):
        if amount > (self.balance + self.limit):
            print(f"{self.holder}: Exceeds overdraft limit!")
        else:
            self.balance -= amount
            print(f"{self.holder} withdrew: {amount}. Balance: {self.balance}")


# Create objects
savings = SavingsAccount("Rahul", 10000, 5)
current = CurrentAccount("Priya", 5000, 2000)


# Savings Account
print("--- Savings Account ---")
savings.deposit(2000)
savings.add_interest()
savings.withdraw(3000)


# Current Account
print("\n--- Current Account ---")
current.withdraw(6000)
current.withdraw(2000)