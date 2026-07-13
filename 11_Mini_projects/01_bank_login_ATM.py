# BANK LOGIN AND ATM

print("WELCOME TO OUR ATM , HAPPY CUSTOMER HAPPY OUR FAMILY❤️")

correct_username = "Mayank kumar"
correct_password = "Maya1234"
balance = 100000

username = input("Enter Your username :")
password = input("Enter your correct password :")
if username == correct_username:
    if password == correct_password:
        print("Login in your Bank successfully.")
        withdraw_amount = int(input("Enter your withdraw amount."))
        if withdraw_amount > 0:
         if balance >= withdraw_amount:
            print("Transaction Successfull.")
            print("Withdraw Amount :", withdraw_amount)
            print("Remaining balance :", balance-withdraw_amount)
         else:
            print("Insufficient balance.")
        else:
            print("Invalid withdraw Amount.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")
    
print(" THANKS FOR USING OUR ATM SYSTEM ")