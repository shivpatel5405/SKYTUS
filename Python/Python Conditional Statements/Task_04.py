# ATM withdrawal check : sufficient balance or not

balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter the amount you want to withdraw: "))
if withdrawal <= balance:
    print(f"Withdrawal of ${withdrawal} is successful. Your new balance is ${balance - withdrawal}.")
else:
    print("Insufficient balance. Withdrawal failed.")
