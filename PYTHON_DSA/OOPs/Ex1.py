# Class Variable

class Student:

    college = "ABC College"

    def __init__(self, name, role_no):
        self.name = name
        self.role_no = role_no

s1 = Student("Vinay", "123")
s2 = Student("Rohit", "124")

print(s1.name, s1.role_no, s1.college)
print(s2.name, s2.role_no, s2.college)