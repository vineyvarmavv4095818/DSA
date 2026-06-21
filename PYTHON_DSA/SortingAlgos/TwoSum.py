def sum(arr, tar):
    n = len(arr)
    i, j = 0, n-1
    arr.sort()

    while(i<j):
        if(arr[i] + arr[j] == tar):
            print("[",arr[i],",",arr[j],"]")
            i += 1
            j -= 1
        
        if(arr[i] + arr[j] > tar):
            j -= 1
        if(arr[i] + arr[j] < tar):
            i -= 1

    return arr
arr = [1,6,2,5,3,4,8,7]
print(sum(arr,9))