class Cow:
    def sound(self):
        print("Moo")

class Lion:
    def sound(self):
        print("Roar")

animals = [Cow(), Lion()]

for animal in animals:
    animal.sound()

'''  1.Yaha bhi sound() same hai, par output object ke according change ho raha hai. 
Yahi Python me polymorphism ka basic idea hai.

2. Yani same method name, different forms (behaviors).
Isi concept ko Polymorphism kehte hain.'''