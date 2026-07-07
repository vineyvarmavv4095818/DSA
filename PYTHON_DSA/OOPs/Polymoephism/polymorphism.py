class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def print_num(self):
        print(self.real,"i +",self.img,"j")

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
      

num1 = Complex(5, 9)
num1.print_num()  

num2 = Complex(4, 6)
num2.print_num()

num3 = num1 - num2
# print(num3.print_num())
num3.print_num()