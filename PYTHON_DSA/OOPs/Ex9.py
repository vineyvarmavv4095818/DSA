class Employee:

    next_id = 101

    def __init__(self, name):
        self.name = name
        self.emp_id = Employee.next_id
        Employee.next_id += 1

e1 = Employee("Vinay")
e2 = Employee("Rohit")
e3 = Employee("Vijay")

print("Employee 1:", e1.emp_id)
print("Employee 2:", e2.emp_id)
print("Employee 3:", e3.emp_id)