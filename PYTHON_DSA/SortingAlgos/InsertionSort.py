def Is(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while(j>0 and arr[j] < arr[j-1]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
        
    return arr

arr = [3,4,5,2,6,7,8,9,1]
print(Is(arr))