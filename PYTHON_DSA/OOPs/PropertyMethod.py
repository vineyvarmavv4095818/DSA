class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def cal_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(90, 98, 94)
print(s1.percentage)

s1.phy = 30
print(s1.percentage)