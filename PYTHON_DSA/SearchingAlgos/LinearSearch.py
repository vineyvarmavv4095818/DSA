def linearSearch(arr,tar):
    n = len(arr)
    for i in range(n):
        if(arr[i]==tar):
            return i
    return -1
    
arr = [23,45,67,87,65,54]
result = linearSearch(arr, 0)

if(result != -1):
    print("Element found at index:",result)
else:
    print("Element not found.")