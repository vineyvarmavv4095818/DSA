class Animal:
    def sound(self):
        print("Animal sounds")

class Dog(Animal):
    def sound(self):
        print("dog barks")

d = Dog()
d.sound()