# Bank Account System

class Account:
    
    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        print("Totle Balance of",self.acc_name,":", self.balance)

a1 = Account("Acc1", 10000)
a2 = Account("Acc2", 20000)

a1.deposit(2000)
a1.get_balance()
a1.withdraw(3000)
a1.get_balance()

a2.deposit(4000)
a2.get_balance()
a2.withdraw(6000)
a2.get_balance()