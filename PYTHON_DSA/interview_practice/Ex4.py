n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):
    count = 2 * i - 1

    if i % 2 != 0:      # Odd row -> print numbers
        for j in range(count):
            print(num, end=" ")
            num += 1
    else:               # Even row -> print #
        for j in range(count):
            print("#", end=" ")

    print()