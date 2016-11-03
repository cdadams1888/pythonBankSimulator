# The BankAccount class simulates a bank account.

class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    # Deposit method makes a deposit into the account.
    def deposit(self, amount):
        self.__balance += amount

    # Withdraw method withdraws an amount from the account.
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount;
        else:
            print('Error: Insufficient funds')

    # getBalance method returns the account balance.
    def getBalance(self):
        return self.__balance
    
