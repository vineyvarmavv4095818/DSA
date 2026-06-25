## Sort the Stack

stack = [4,1,5,2,7,8]
temp = []

while stack != []:

    x = stack.pop()

    while temp!=[] and temp[-1]>x:
        stack.append(temp.pop())

    temp.append(x)

print(temp)