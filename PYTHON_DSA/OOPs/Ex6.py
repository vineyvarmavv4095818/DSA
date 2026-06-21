class Book:

    def __init__(self, title):
        self.title = title

    def display(self):
        print("Book :", self.title)

b1 = Book("Python")
b2 = Book("Java")

b1.display()
b2.display()