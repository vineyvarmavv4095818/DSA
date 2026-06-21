# basic example of abstraction

from abc import ABC, abstractmethod

class Animal(ABC): #Abstract class

    @abstractmethod
    def sound(self):  #abstractMethod ka implemetation nahi krte.
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()

