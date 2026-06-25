## Revrse Stack

st = [1,2,3,4,5]
temp = []

while st:
    temp.append(st.pop())

st = temp

print(st)