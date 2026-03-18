# ATM transaction validation with balance check, PIN verification, and withdrawal limit

account_balance = int(input("Account Balance: "))
withdrawal_amount = int(input("Withdrawal Amount: "))
entered_pin = int(input("Enter PIN: "))

correct_pin = 444303

if account_balance >= withdrawal_amount:
    if entered_pin == correct_pin:
        if withdrawal_amount <= 25000:
            print("Transaction Successful")
        else:
            print("Daily Limit Exceeded")
    else:
        print("Wrong PIN")
else:
    print("Insufficient Balance")