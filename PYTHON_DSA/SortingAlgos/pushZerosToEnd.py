def push(arr):
    n = len(arr)
    for i in range(0, n-1):
        isDone = True
        for j in range(0, n-1-i):
            if(arr[j]==0):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                isDone = False

        if(isDone==True): break

    return arr

arr = [2,-9,4,1,5,0,3,0,-4,2,0]
print(push(arr))