## Sum of odd numbers of a list


list = [1, 3, 6, 8, 2, 9, 4, 3]

sum = 0
for i in range(len(list)):
    if list[i] % 2 != 0:
        sum += list[i]

print(sum)