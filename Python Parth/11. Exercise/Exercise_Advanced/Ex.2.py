# bank_account_system.py

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        """
        Initialize a bank account with an account number, account holder, and initial balance.

        :param account_number: str
        :param account_holder: str
        :param initial_balance: float (default=0.0)
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: float
        :return: float (new balance)
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transaction_history.append({"type": "deposit", "amount": amount})
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        :param amount: float
        :return: float (new balance)
        :raises: ValueError if insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append({"type": "withdrawal", "amount": amount})
        return self.balance

    def get_balance(self):
        """
        Get the current account balance.

        :return: float
        """
        return self.balance

    def get_transaction_history(self):
        """
        Get the transaction history of the account.

        :return: list of dicts
        """
        return self.transaction_history

    def __str__(self):
        """
        Return a string representation of the account.

        :return: str
        """
        return f"Account {self.account_number} - {self.account_holder}: {self.balance:.2f}"


class Bank:
    def __init__(self):
        """
        Initialize a bank with an empty list of accounts.
        """
        self.accounts = []

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        """
        Create a new bank account.

        :param account_number: str
        :param account_holder: str
        :param initial_balance: float (default=0.0)
        :return: BankAccount
        """
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts.append(account)
        return account

    def get_account(self, account_number):
        """
        Get an account by its account number.

        :param account_number: str
        :return: BankAccount or None
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def __str__(self):
        """
        Return a string representation of the bank.

        :return: str
        """
        return f"Bank with {len(self.accounts)} accounts"


def main():
    bank = Bank()

    while True:
        print("Bank Account System")
        print("1. Create Account")
        print("2. Login to Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance (default=0.0): ") or 0.0)
            account = bank.create_account(account_number, account_holder, initial_balance)
            print(f"Account created: {account}")

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                while True:
                    print("Account Menu")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        amount = float(input("Enter deposit amount: "))
                        try:
                            account.deposit(amount)
                            print(f"Deposit successful. New balance: {account.balance:.2f}")
                        except ValueError as e:
                            print(f"Error: {e}")

                    elif choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        try:
                            account.withdraw(amount)
                            print(f"Withdrawal successful. New balance: {account.balance:.2f}")
                        except ValueError as e:
                            print(f"Error: {e}")

                    elif choice == "3":
                        print(f"Current balance: {account.balance:.2f}")

                    elif choice == "4":
                        print("Transaction History:")
                        for transaction in account.transaction_history:
                           print(f"{transaction['type'].capitalize()}: {transaction['amount']:.2f}")

                    elif choice == "5":
                        break

            else:
                print("Account not found")

        elif choice == "3":
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()