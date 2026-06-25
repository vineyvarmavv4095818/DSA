## Reverse String

s = "Vinay"
stack = []

for i in s:
    stack.append(i)

ans = ""

while stack:
    x = stack.pop()
    ans += x

print(ans)