# Multilevel Inheritance

class GRandParent:
    def show1(self):
        print("Grand Parente")

class Parent(GRandParent):
    def show2(self):
        print("Parent")

class Child(Parent):
    def show3(self):
        print("Child")

c = Child()

c.show1()
c.show2()
c.show3()