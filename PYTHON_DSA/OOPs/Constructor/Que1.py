class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
cir1 = Circle(21)
print(cir1.area())
print(cir1.perimeter())