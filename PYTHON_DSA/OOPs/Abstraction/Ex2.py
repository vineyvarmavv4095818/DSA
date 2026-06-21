from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * (self.r ** 2)

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

c = Circle(5)
r = Rectangle(2, 5)

print(c.area())
print(r.area())