n = int(input("Enter a number:"))

num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        if j % 2 != 0:
            print(num%10, end=" ")
            num += 1
        else:
            print("*", end=" ")
    
    print()