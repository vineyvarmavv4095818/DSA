n = int(input("Enter a number:"))

num = 1

for i in range(1, n+1):
    print(" " * (2*(n-i)), end=" ")

    if i % 2 != 0:
        for j in range(2*i-1):
            print(num, end=" ")
            num += 1
        
    else:
        for j in range(2*i-1):
            print("#", end=" ")

    print()