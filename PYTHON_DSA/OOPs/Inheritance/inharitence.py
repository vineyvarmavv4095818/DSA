class Car:
    color = "white"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")

class Bugatti(Car):
    def __init__(self, name):
        self.name = name

car1 = Bugatti("chiron") 
car2 = Bugatti("viron")

print(car1.start())
print(car1.name)

print(car1.color)
print(car2.color)
            