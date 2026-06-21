# Class Method

class Student:

    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def total_student(cls):
        return cls.count

s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()

print(Student.total_student())
