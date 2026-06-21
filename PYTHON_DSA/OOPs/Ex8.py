# code 1

class Marks:
    def __init__(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem

    def average(self):
        return (self.math + self.phy + self.chem)/3

s = Marks(90, 99, 90)
print(s.average())

# code 2

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

s = Student("Vinay", [80, 90, 85])

print(s.percentage())