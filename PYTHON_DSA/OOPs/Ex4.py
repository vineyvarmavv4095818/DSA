#super() Function

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role :", self.role)
        print("Department :", self.dept)
        print("Salary :", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "Rs.75,000")

    def showDetails(self):
        super().showDetails() # Employee class function

        print("Name :", self.name)
        print("Age :", self.age)

eng1 = Engineer("Vinay Verma", 25)
eng1.showDetails()