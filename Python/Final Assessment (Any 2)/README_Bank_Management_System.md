# 🏦 Bank Management System

A terminal-based banking application built in Python that simulates core banking operations — account creation, deposits, withdrawals, transfers, and transaction tracking — all from the command line.

---

## 📋 Table of Contents

- [Features](#features)
- [How to Run](#how-to-run)
- [Menu Options](#menu-options)
- [Account Details](#account-details)
- [Banking Rules](#banking-rules)
- [Transaction Logging](#transaction-logging)
- [Project Structure](#project-structure)
- [Requirements](#requirements)

---

## ✨ Features

- **Account Management** — Create, view, search, and close bank accounts
- **Deposits & Withdrawals** — Deposit or withdraw funds with balance validation
- **Fund Transfers** — Transfer money between any two accounts
- **Transaction History** — Full chronological log per account with timestamps
- **Account Search** — Look up accounts by customer name (partial match supported)
- **Account Listing** — View all accounts with a summary of total deposits
- **Input Validation** — Robust handling of invalid inputs across all operations
- **Confirmation Prompts** — Withdrawals, transfers, and closures require explicit confirmation
- **Formatted Display** — Clean ASCII-styled cards, tables, and banners

---

## 🚀 How to Run

**Prerequisites:** Python 3.x

```bash
python Bank_Management_System.py
```

No external libraries are required — the system uses only the built-in `random` and `time` modules.

---

## 🗂️ Menu Options

| Option | Action                    | Description                                          |
| ------ | ------------------------- | ---------------------------------------------------- |
| 1      | Create New Account        | Register a new customer with name, phone, and deposit |
| 2      | View Account Details      | Display full account card by account number          |
| 3      | Deposit Money             | Add funds to an existing account                     |
| 4      | Withdraw Money            | Withdraw funds (maintains minimum balance)           |
| 5      | Transfer Money            | Move funds between two accounts                      |
| 6      | View Transaction History  | See all transactions for a specific account          |
| 7      | List All Accounts         | Display a table of every account in the system       |
| 8      | Search Account by Name    | Find accounts by partial or full name match          |
| 9      | Close an Account          | Permanently delete an account and return balance     |
| 0      | Exit                      | Quit the application                                 |

---

## 📇 Account Details

Each account stores the following information:

| Field            | Description                                    |
| ---------------- | ---------------------------------------------- |
| Account Number   | Auto-generated unique 8-digit number           |
| Account Holder   | Full name of the customer                      |
| Phone Number     | Contact number (minimum 10 digits)             |
| Account Type     | Savings or Current                             |
| Balance          | Current balance in Rs.                         |
| Opened On        | Timestamp of account creation                  |

---

## 📏 Banking Rules

| Rule                  | Detail                                                    |
| --------------------- | --------------------------------------------------------- |
| Minimum Initial Deposit | Rs. 500                                                 |
| Minimum Balance       | Rs. 500 must be maintained at all times                   |
| Withdrawal Limit      | Up to `balance − 500` (preserves minimum balance)         |
| Transfer Limit        | Same as withdrawal — sender must retain Rs. 500           |
| Self-Transfer         | Not allowed (sender and receiver must differ)             |
| Account Closure       | Requires typing `CLOSE` to confirm; returns full balance  |

---

## 📜 Transaction Logging

Every operation is recorded in a transaction log with the following fields:

| Field    | Example                  |
| -------- | ------------------------ |
| Account  | `84729361`               |
| Type     | Deposit / Withdrawal / Transfer In / Transfer Out / Account Created / Account Closed |
| Amount   | `1500.00`                |
| Balance  | `3500.00` (post-transaction) |
| Time     | `2026-09-25 12:15:30`    |

Use **Menu Option 6** to view the full transaction history for any account.

---

## 📁 Project Structure

```
Final Assessment (Any 2)/
├── Bank_Management_System.py          # Main application script
└── README_Bank_Management_System.md   # This file
```

### Key Functions

| Function                  | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| `generate_account_number()` | Generates a unique random 8-digit account number       |
| `get_timestamp()`         | Returns the current date/time as a formatted string      |
| `log_transaction()`       | Records a transaction entry to the global log            |
| `find_account()`          | Looks up an account by number, returns data or `None`    |
| `get_valid_amount()`      | Input loop that ensures a valid positive number          |
| `get_account_input()`     | Prompts for account number and validates existence       |
| `display_banner()`        | Renders the ASCII welcome banner                         |
| `display_menu()`          | Prints the main menu with all 10 options                 |
| `display_account_card()`  | Formats and prints account details as a bordered card    |
| `create_account()`        | Full account creation workflow with validation           |
| `view_account()`          | Displays a single account's details                      |
| `deposit_money()`         | Handles deposit with balance update and logging          |
| `withdraw_money()`        | Handles withdrawal with min-balance check and confirmation |
| `transfer_money()`        | Moves funds between accounts with dual logging           |
| `view_transactions()`     | Displays filtered transaction history table              |
| `list_all_accounts()`     | Prints a summary table of all accounts                   |
| `search_by_name()`        | Searches accounts by partial name match                  |
| `close_account()`         | Deletes an account after confirmation                    |
| `run_bank()`              | Main loop — displays menu and routes user choices        |

---

## 📦 Requirements

- **Python** 3.x
- **Modules:** `random`, `time` (both part of the Python standard library)

No installation of third-party packages is needed.

---

## ⚠️ Notes

- All data is stored **in-memory** — accounts and transactions are lost when the program exits.
- Account numbers are randomly generated and guaranteed unique within a session.
- Currency is displayed in **Rs.** (Indian Rupees).

---

## 📝 License

This project was created as part of a Python Final Assessment.
