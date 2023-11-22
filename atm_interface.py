import random as r
import sys
class ATM():
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Nu.{self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def display_transaction_history(self):
        print("Transaction History:")
        for transactions in self.transaction_history:
            print(transactions)

    def check_balance(self):
        print("Available balance: Nu.", self.balance)
        print()

    def transaction(self):
        print("-------------********** Welcome to the JS ATM **********-------------")
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Transaction History
            6. Exit
        *********************
        """)

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4, 5,or 6:"))
            except:
                print("Error: Select the transaction: 1, 2, 3, 4, 5,or 6 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    atm.display_transaction_history()
                elif option == 6:
                    print(f"""
                                printing receipt..............
                          ******************************************
                              Transaction is now complete.                         
                              Transaction number: {r.randint(10000, 1000000)} 
                              Account holder: {self.name.upper()}                  
                              Account number: {self.account_number}                
                              Available balance: Nu.{self.balance}                    

                              Thanks for choosing us as your bank                  
                          ******************************************
                          """)
                    sys.exit()


print("----------******* WELCOME TO JS BANK OF INDIA *******----------")
print("======================================================\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
pin = int(input("create pin:"))
account_number = [r.randint(6, 9)]
for i in range(1, 10):
    account_number.append(r.randint(0, 9))
for i in account_number:
    print(i, end="")
print("Congratulations! Account created successfully......\n")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")