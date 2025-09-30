import sys
from datetime import datetime

class BankAccount:
    def __init__(self, name, acc_number, balance=0.0):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Invalid deposit amount.")
            return
        self.balance += amount
        self.transactions.append((datetime.now(), f"Deposited {amount}"))
        print(f"✅ {amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
            return
        self.balance -= amount
        self.transactions.append((datetime.now(), f"Withdrew {amount}"))
        print(f"✅ {amount} withdrawn successfully.")

    def show_balance(self):
        print(f"💰 Current Balance: {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("📂 No transactions yet.")
        else:
            print("📜 Transaction History:")
            for t in self.transactions[-20:]:
                print(f"{t[0].strftime('%Y-%m-%d %H:%M:%S')} - {t[1]}")

def main():
    print("=== 🏦 Welcome to Terminal Banking App ===")

    name = input("Enter account holder name: ")
    acc_number = input("Enter account number: ")
    account = BankAccount(name, acc_number)

    while True:
        print("\n--- MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            account.show_balance()
        elif choice == '4':
            account.show_transactions()
        elif choice == '5':
            print("👋 Thank you for using Terminal Banking. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()

