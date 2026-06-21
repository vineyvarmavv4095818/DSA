# Private vairable

class Account:
    def __init__(self, acc_num, acc_pass):
        self.acc_num = acc_num
        self.__acc_pass = acc_pass

    def showDetails(self):
        print(self.__acc_pass)

a = Account(12345, "abcde")

a.showDetails()