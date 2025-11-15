"""B2. Write a program menu driven to create a BankAccount class. class should
support the following methods for
i) Deposit
ii) Withdraw
iii) GetBalanace
Create a subclass SavingsAccount class that behaves just like a BankAccount, but
also has an interest rate and a method that increases the balance by the
appropriate amount of interest."""

import sys


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= min(amount, self.balance)
            print("Amount withdrawn.")
        else:
            print("Insufficient balance..!")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self.balance *= 1 + self.interest_rate / 100
        print("Interest added.")


account = SavingsAccount(interest_rate=2)
while True:
    choice = input(
        "\n1. Deposit\n2. Withdraw\n3. Get Balance\n4. Add Interest\n5.Exit\nEnter your choice: "
    )
    if choice == "1":
        account.deposit(float(input("Enter the amount to deposit: ")))
    elif choice == "2":
        account.withdraw(float(input("Enter the amount to withdraw: ")))
    elif choice == "3":
        print("Account balance: ", account.get_balance())
    elif choice == "4":
        account.calculate_interest()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
