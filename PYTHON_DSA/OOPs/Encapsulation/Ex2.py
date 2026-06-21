# Deposit Money

class Bank:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        print(self.__balance)

b = Bank()

b.deposit(5000)

b.get_balance()