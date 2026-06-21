def ss(arr):
    n = len(arr)
    for i in range(n):
        min = float('inf')
        mindex = -1
        for j in range(i,n):
            if(arr[j] < min):
                min = arr[j]
                mindex = j

        temp = arr[i]
        arr[i] = arr[mindex]
        arr[mindex] = temp

    return arr

arr = [5,3,4,1,2]
print(ss(arr))
