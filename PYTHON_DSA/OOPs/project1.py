class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    #debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs",amount,"are debited")
        print("total balance is", self.get_balance())

    #credit
    def credit(self, amount):
        self.balance += amount
        print("Rs",amount,"are credited")
        print("total balance is", self.get_balance())

    def get_balance(self):    #function for final balance
        return self.balance
    
print("DETAIL OF ACCOUNT A:\n")

x = int(input("enter balance for debit:"))
acc1 = Account(10000, "A")
acc1.debit(x)
acc1.credit(500)

print("\nDETAIL OF ACCOUNT B:\n")

y = int(input("enter balance for debit:"))
acc2 = Account(20000, "B")
acc2.debit(y)
acc2.credit(50)