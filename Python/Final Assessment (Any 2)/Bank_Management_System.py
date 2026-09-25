# Bank Management System

import random
import time


# Dictionary to store all accounts:
accounts = {}

# List to store transaction history
transaction_log = []


# ---------- Helper Functions ----------

def generate_account_number():
    """Generate a unique 8-digit account number."""
    while True:
        acc_no = str(random.randint(10000000, 99999999))
        if acc_no not in accounts:
            return acc_no


def get_timestamp():
    """Get the current date and time as a readable string."""
    return time.strftime("%Y-%m-%d %H:%M:%S")


def log_transaction(acc_no, txn_type, amount, balance):
    """Record a transaction in the transaction log."""
    entry = {
        "account": acc_no,
        "type": txn_type,
        "amount": amount,
        "balance": balance,
        "time": get_timestamp()
    }
    transaction_log.append(entry)


def find_account(acc_no):
    """Find and return account data, or None if not found."""
    if acc_no in accounts:
        return accounts[acc_no]
    else:
        return None


def get_valid_amount(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("  Amount must be greater than zero.")
            else:
                return round(amount, 2)
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_account_input():
    """Ask the user for an account number and find the account."""
    acc_no = input("  Enter account number: ").strip()
    account = find_account(acc_no)
    if account is None:
        print(f"\n  >> Account '{acc_no}' not found.\n")
        return None, None
    return acc_no, account


# ---------- Display Functions ----------

def display_banner():
    """Display the welcome banner."""
    print()
    print("=" * 55)
    print("|                                                     |")
    print("|        *  BANK MANAGEMENT SYSTEM  *                 |")
    print("|                                                     |")
    print("|   Manage accounts, deposits, withdrawals & more!    |")
    print("|   Your money, your control.                         |")
    print("|                                                     |")
    print("=" * 55)
    print()


def display_menu():
    """Display the main menu options."""
    print("-" * 40)
    print("  MAIN MENU")
    print("-" * 40)
    print("  1) Create New Account")
    print("  2) View Account Details")
    print("  3) Deposit Money")
    print("  4) Withdraw Money")
    print("  5) Transfer Money")
    print("  6) View Transaction History")
    print("  7) List All Accounts")
    print("  8) Search Account by Name")
    print("  9) Close an Account")
    print("  0) Exit")
    print("-" * 40)


def display_account_card(acc_no, account):
    """Display account details in a formatted card."""
    print()
    print("+" + "-" * 45 + "+")
    print(f"|  Account Number  : {acc_no:<25}|")
    print(f"|  Account Holder  : {account['name']:<25}|")
    print(f"|  Account Type    : {account['type']:<25}|")
    print(f"|  Balance         : Rs. {account['balance']:<21}|")
    print(f"|  Phone           : {account['phone']:<25}|")
    print(f"|  Opened On       : {account['created']:<25}|")
    print("+" + "-" * 45 + "+")
    print()


# ---------- Core Banking Functions ----------

def create_account():
    """Create a new bank account."""
    print()
    print("  --- Create New Account ---")
    print()

    # Get customer name
    name = input("  Enter full name: ").strip()
    if name == "":
        print("  >> Name cannot be empty.\n")
        return

    # Get phone number
    phone = input("  Enter phone number: ").strip()
    if phone == "" or not phone.isdigit() or len(phone) < 10:
        print("  >> Please enter a valid phone number (at least 10 digits).\n")
        return

    # Choose account type
    print("  Choose account type:")
    print("    1) Savings")
    print("    2) Current")
    while True:
        try:
            type_choice = int(input("  Enter choice (1 or 2): "))
            if type_choice == 1:
                acc_type = "Savings"
                break
            elif type_choice == 2:
                acc_type = "Current"
                break
            else:
                print("  Please enter 1 or 2.")
        except ValueError:
            print("  Please enter a valid number.")

    # Get initial deposit
    print()
    min_deposit = 500.0
    print(f"  Minimum initial deposit: Rs. {min_deposit}")
    while True:
        deposit = get_valid_amount("  Enter initial deposit amount: Rs. ")
        if deposit < min_deposit:
            print(f"  >> Minimum deposit is Rs. {min_deposit}. Try again.")
        else:
            break

    # Generate account number and store account
    acc_no = generate_account_number()
    accounts[acc_no] = {
        "name": name,
        "phone": phone,
        "type": acc_type,
        "balance": deposit,
        "created": get_timestamp()
    }

    # Log the transaction
    log_transaction(acc_no, "Account Created", deposit, deposit)

    print()
    print("  " + "=" * 40)
    print("  >> Account created successfully!")
    print(f"  >> Account Number: {acc_no}")
    print(f"  >> Name: {name}")
    print(f"  >> Type: {acc_type}")
    print(f"  >> Balance: Rs. {deposit}")
    print("  " + "=" * 40)
    print("  >> Please remember your account number!")
    print()


def view_account():
    """View details of a specific account."""
    print()
    print("  --- View Account Details ---")
    print()

    acc_no, account = get_account_input()
    if account is None:
        return

    display_account_card(acc_no, account)


def deposit_money():
    """Deposit money into an account."""
    print()
    print("  --- Deposit Money ---")
    print()

    acc_no, account = get_account_input()
    if account is None:
        return

    print(f"  Current Balance: Rs. {account['balance']}")
    amount = get_valid_amount("  Enter deposit amount: Rs. ")

    # Update balance
    account["balance"] = round(account["balance"] + amount, 2)

    # Log the transaction
    log_transaction(acc_no, "Deposit", amount, account["balance"])

    print()
    print(f"  >> Rs. {amount} deposited successfully!")
    print(f"  >> New Balance: Rs. {account['balance']}")
    print()


def withdraw_money():
    """Withdraw money from an account."""
    print()
    print("  --- Withdraw Money ---")
    print()

    acc_no, account = get_account_input()
    if account is None:
        return

    print(f"  Current Balance: Rs. {account['balance']}")

    min_balance = 500.0
    available = round(account["balance"] - min_balance, 2)

    if available <= 0:
        print(f"  >> Insufficient funds. Minimum balance of Rs. {min_balance} must be maintained.")
        print()
        return

    print(f"  Available for withdrawal: Rs. {available}")

    while True:
        amount = get_valid_amount("  Enter withdrawal amount: Rs. ")
        if amount > available:
            print(f"  >> Cannot withdraw Rs. {amount}. Maximum available: Rs. {available}")
        else:
            break

    # Confirmation
    confirm = input(f"  Confirm withdrawal of Rs. {amount}? (yes/no): ").lower().strip()
    if confirm not in ["yes", "y"]:
        print("  >> Withdrawal cancelled.\n")
        return

    # Update balance
    account["balance"] = round(account["balance"] - amount, 2)

    # Log the transaction
    log_transaction(acc_no, "Withdrawal", amount, account["balance"])

    print()
    print(f"  >> Rs. {amount} withdrawn successfully!")
    print(f"  >> New Balance: Rs. {account['balance']}")
    print()


def transfer_money():
    """Transfer money from one account to another."""
    print()
    print("  --- Transfer Money ---")
    print()

    # Source account
    print("  [From Account]")
    from_no = input("  Enter sender account number: ").strip()
    from_acc = find_account(from_no)
    if from_acc is None:
        print(f"  >> Sender account '{from_no}' not found.\n")
        return

    # Destination account
    print("  [To Account]")
    to_no = input("  Enter receiver account number: ").strip()
    to_acc = find_account(to_no)
    if to_acc is None:
        print(f"  >> Receiver account '{to_no}' not found.\n")
        return

    # Cannot transfer to same account
    if from_no == to_no:
        print("  >> Cannot transfer to the same account.\n")
        return

    print()
    print(f"  Sender   : {from_acc['name']} (Balance: Rs. {from_acc['balance']})")
    print(f"  Receiver : {to_acc['name']}")

    min_balance = 500.0
    available = round(from_acc["balance"] - min_balance, 2)

    if available <= 0:
        print(f"  >> Insufficient funds. Minimum balance of Rs. {min_balance} must be maintained.")
        print()
        return

    print(f"  Available for transfer: Rs. {available}")

    while True:
        amount = get_valid_amount("  Enter transfer amount: Rs. ")
        if amount > available:
            print(f"  >> Cannot transfer Rs. {amount}. Maximum available: Rs. {available}")
        else:
            break

    # Confirmation
    confirm = input(f"  Confirm transfer of Rs. {amount} to {to_acc['name']}? (yes/no): ").lower().strip()
    if confirm not in ["yes", "y"]:
        print("  >> Transfer cancelled.\n")
        return

    # Update both balances
    from_acc["balance"] = round(from_acc["balance"] - amount, 2)
    to_acc["balance"] = round(to_acc["balance"] + amount, 2)

    # Log for both accounts
    log_transaction(from_no, "Transfer Out", amount, from_acc["balance"])
    log_transaction(to_no, "Transfer In", amount, to_acc["balance"])

    print()
    print(f"  >> Rs. {amount} transferred successfully!")
    print(f"  >> {from_acc['name']}'s Balance: Rs. {from_acc['balance']}")
    print(f"  >> {to_acc['name']}'s Balance: Rs. {to_acc['balance']}")
    print()


def view_transactions():
    """View transaction history for an account."""
    print()
    print("  --- Transaction History ---")
    print()

    acc_no, account = get_account_input()
    if account is None:
        return

    # Filter transactions for this account
    acc_transactions = []
    for txn in transaction_log:
        if txn["account"] == acc_no:
            acc_transactions.append(txn)

    if len(acc_transactions) == 0:
        print("  >> No transactions found for this account.\n")
        return

    print(f"  Account: {account['name']} ({acc_no})")
    print()
    print("  " + "-" * 65)
    print(f"  {'No.':<5}{'Type':<18}{'Amount (Rs.)':<15}{'Balance (Rs.)':<15}{'Date & Time'}")
    print("  " + "-" * 65)

    for i in range(len(acc_transactions)):
        txn = acc_transactions[i]
        print(f"  {i + 1:<5}{txn['type']:<18}{txn['amount']:<15}{txn['balance']:<15}{txn['time']}")

    print("  " + "-" * 65)
    print(f"  Total Transactions: {len(acc_transactions)}")
    print()


def list_all_accounts():
    """List all accounts in the system."""
    print()
    print("  --- All Accounts ---")
    print()

    if len(accounts) == 0:
        print("  >> No accounts found. Create one first!\n")
        return

    print("  " + "-" * 70)
    print(f"  {'No.':<5}{'Acc. Number':<14}{'Name':<20}{'Type':<12}{'Balance (Rs.)'}")
    print("  " + "-" * 70)

    i = 1
    total_balance = 0
    for acc_no in accounts:
        acc = accounts[acc_no]
        print(f"  {i:<5}{acc_no:<14}{acc['name']:<20}{acc['type']:<12}{acc['balance']}")
        total_balance += acc["balance"]
        i += 1

    print("  " + "-" * 70)
    print(f"  Total Accounts: {len(accounts)}    |    Total Deposits: Rs. {round(total_balance, 2)}")
    print()


def search_by_name():
    """Search for accounts by customer name."""
    print()
    print("  --- Search Account by Name ---")
    print()

    search_name = input("  Enter name to search: ").strip().lower()
    if search_name == "":
        print("  >> Please enter a name to search.\n")
        return

    # Find matching accounts
    results = []
    for acc_no in accounts:
        if search_name in accounts[acc_no]["name"].lower():
            results.append(acc_no)

    if len(results) == 0:
        print(f"  >> No accounts found matching '{search_name}'.\n")
        return

    print(f"  Found {len(results)} account(s):\n")
    for acc_no in results:
        display_account_card(acc_no, accounts[acc_no])


def close_account():
    """Close (delete) a bank account."""
    print()
    print("  --- Close Account ---")
    print()

    acc_no, account = get_account_input()
    if account is None:
        return

    display_account_card(acc_no, account)

    print(f"  >> WARNING: This will permanently close the account!")
    print(f"  >> Remaining balance of Rs. {account['balance']} will be returned.\n")

    confirm = input("  Type 'CLOSE' to confirm: ").strip()
    if confirm != "CLOSE":
        print("  >> Account closure cancelled.\n")
        return

    # Log the closure
    log_transaction(acc_no, "Account Closed", account["balance"], 0)

    # Remove the account
    del accounts[acc_no]

    print()
    print(f"  >> Account {acc_no} has been closed.")
    print(f"  >> Rs. {account['balance']} has been returned to the customer.")
    print()


# ---------- Main Program ----------

def run_bank():
    """Run the Bank Management System."""
    display_banner()

    running = True

    while running:
        display_menu()

        choice = input("  Enter your choice: ").strip()
        print()

        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            view_transactions()
        elif choice == "7":
            list_all_accounts()
        elif choice == "8":
            search_by_name()
        elif choice == "9":
            close_account()
        elif choice == "0":
            print("  " + "=" * 40)
            print("  Thank you for using Bank Management System!")
            print("  Have a great day!")
            print("  " + "=" * 40)
            print()
            running = False
        else:
            print("  >> Invalid choice. Please enter 0 to 9.\n")

        # Pause before showing menu again (except on exit)
        if running:
            input("  Press Enter to continue...")
            print()


# ---------- Start the Program ----------
run_bank()