n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

print()

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

print()

for i in range(n+1):
    for k in range(n-i):
        print(' ', end=' ')
    for j in range(2*i+1):
        print('*', end=' ')
    print()

print()

for i in range(n, -1, -1):
    for k in range(n-i):
        print(' ', end=' ')
    for j in range(2*i+1):
        print('*', end=' ')
    print()

print()

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

print()

num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=' ')
        num += 1
    print()

print()

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()