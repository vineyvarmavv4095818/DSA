def reverse(list, i, j):
    if(i>=j):
        return
    
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

    return reverse(list, i+1, j-1)

list = [1,2,3,4,5,6]
n = len(list)
print(list)
reverse(list, 0, n-1)

print(list)