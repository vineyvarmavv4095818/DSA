def solve(bills):
    five = 0
    ten = 0

    for i in range(0, len(bills)):
        if bills[i] == 5:
            five += 1

        elif bills[i] == 10:
            if five >= 1:
                five -= 1
                ten += 1
            else:
                return False

        else:
            if five >= 1 and ten >= 1:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


bills = [5,5,5,10,20]
print(solve(bills))


# TC = O(n)
# SC = O(1)
