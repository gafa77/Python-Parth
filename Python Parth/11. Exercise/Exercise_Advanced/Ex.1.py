class BankAccount:
    def __init__(self, account_id, pin, account_type):
        self.account_id = account_id
        self.pin = pin
        self.account_type = account_type
        self.balance = 0

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} credited to your account. New balance: Rs. {self.balance}")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs. {amount} debited from your account. New balance: Rs. {self.balance}")

    def update_pin(self, new_pin):
        self.pin = new_pin
        print("PIN updated successfully!")

    def check_balance(self):
        print(f"Your current balance is: Rs. {self.balance}")

def main():
    print("Choose your bank:")
    print("1. HDFC")
    print("2. AXIS")
    print("3. SBI")
    bank_choice = int(input("Enter your choice (1/2/3): "))

    if bank_choice == 1:
        bank_name = "HDFC"
    elif bank_choice == 2:
        bank_name = "AXIS"
    else:
        bank_name = "SBI"

    account_id = input("Enter your account ID: ")
    pin = input("Enter your PIN: ")

    print("Choose your account type:")
    print("1. Savings")
    print("2. Current")
    account_type_choice = int(input("Enter your choice (1/2): "))

    if account_type_choice == 1:
        account_type = "Savings"
    else:
        account_type = "Current"

    account = BankAccount(account_id, pin, account_type)

    while True:
        print("\nChoose an option:")
        print("1. Credit")
        print("2. Debit")
        print("3. Update PIN")
        print("4. Check Balance")
        print("5. Exit")
        option = int(input("Enter your choice (1/2/3/4/5): "))

        if option == 1:
            amount = float(input("Enter amount to credit: "))
            account.credit(amount)
        elif option == 2:
            amount = float(input("Enter amount to debit: "))
            account.debit(amount)
        elif option == 3:
            new_pin = input("Enter new PIN: ")
            account.update_pin(new_pin)
        elif option == 4:
            account.check_balance()
        elif option == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()