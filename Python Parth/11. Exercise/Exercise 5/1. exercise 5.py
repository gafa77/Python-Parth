class Bank:
    def __init__(self, name, age, amount):
        self.name = name
        self.age = age
        self.amount = amount

    def debitAmount(self, value):
        if value > self.amount:
            print("Insufficient balance")
        else:
            self.amount -= value
            print("Amount after debit is", self.amount)

    def creditAmount(self, value):
        self.amount += value
        print("Amount after credit is", self.amount)

    def getBalance(self):
        return self.amount

B1 = Bank("Parth Badgujar", 17, 10000)
B1.debitAmount(2000)
B1.creditAmount(5000)
print("Current balance is", B1.getBalance())














"""class BankAccount:
    def __init__(self, name, pin, amount):
        self.name = name
        self.pin = pin
        self.amount = amount

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            return True
        else:
            return False

    def show_details(self):
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.amount}")

    def update_amount(self):
        while True:
            transaction_type = input("Do you want to debit or credit? (debit/credit): ")
            if transaction_type == "debit":
                value = float(input("Enter the amount to debit: "))
                if self.amount >= value:
                    self.amount -= value
                    print(f"Amount debited successfully. New amount: {self.amount}")
                    break
                else:
                    print("Insufficient balance.")
            elif transaction_type == "credit":
                value = float(input("Enter the amount to credit: "))
                self.amount += value
                print(f"Amount credited successfully. New amount: {self.amount}")
                break
            response = input("Do you want to try again or cancel? (try again/cancel): ")
            if response.lower() == "cancel":
                print("Transaction cancelled.")
                break

def main():
    account = BankAccount("Parth Badgujar", "2007", 1000.0)

    while True:
        name = input("Enter your account name: ")
        pin = input("Enter your PIN: ")

        if name == account.name and account.check_pin(pin):
            print("Login successful!")
            account.show_details()

            while True:
                account.update_amount()
                response = input("Do you want to perform another transaction? (yes/no): ")
                if response.lower() == "no":
                    print("Thank you for your services!")
                    break
            break
        else:
            print("Invalid account name or PIN. Please try again.")

if __name__ == "__main__":
    main()"""
