class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  #private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount},  New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

# Testing the BankAccount class
account = BankAccount("Swasti", 1000)
account.deposit(5000)
account.withdraw(300)
account.withdraw(1500) 
account.withdraw(5000)
print("Final Balance:", account.get_balance())
