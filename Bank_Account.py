class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful:", amount)
        else:
            print("Transfer failed! Insufficient balance or invalid amount.")



account1 = BankAccount("Atharv")
account2 = BankAccount("Rahul")


account1.deposit(5000)
account2.deposit(3000)


account1.withdraw(1000)


account1.transfer(2000, account2)


print("\nAccount 1 Details:")
account1.display_balance()

print("\nAccount 2 Details:")
account2.display_balance()