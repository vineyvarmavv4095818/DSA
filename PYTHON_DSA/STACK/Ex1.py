## Copy stack into another in same order:

s1 = [1,2,3,4,5]

temp = []
s2 = []

while s1:  # Here, we can write (1)s1: (2)len(s1) > 0: (3)s1 != []:
    temp.append(s1.pop())

while temp != []:

    y = temp.pop()
    s1.append(y)
    s2.append(y)

print("s1:", s1)
print("s2:", s2)