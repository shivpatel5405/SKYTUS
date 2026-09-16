# Create a BankAccount class with deposit and withdraw methods

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount to be deposited is: {amount}")
        print(f"Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount to be withdrawn: {amount}")
            print(f"Current balance After Withdrawal is: {self.balance}")


# Create an object
account1 = BankAccount("Martinez", 10000)

# Display account information
print(f"The name of Account Holder: {account1.account_holder}")
print(f"Initial Balance: {account1.balance}")

# Deposit money
account1.deposit(5000)

# Withdraw money
account1.withdraw(3000)