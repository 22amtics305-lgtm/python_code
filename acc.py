account_balance = 5000
print("Your current balance is: Rs", account_balance)

withdrawal_amount = int(input("Enter the amount to withdraw: "))

if withdrawal_amount % 100 != 0:
    print("Failure: Amount must be a multiple of 100 (e.g., 100, 200, 500).")

elif account_balance - withdrawal_amount < 1000:
    print("Failure: Insufficient balance! You must leave a minimum of Rs 1000 in your account.")

else:
    account_balance = account_balance - withdrawal_amount
    print("Success: Please collect your cash!")
    print("Remaining Balance: Rs", account_balance)