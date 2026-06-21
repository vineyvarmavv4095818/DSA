def search(list, target):
    
    lo, hi = 0, len(list)-1

    while(lo <= hi):
        mid = (lo+hi)//2
        if(target == list[mid]):
            return mid
        elif(target > list[mid]):
            lo = mid + 1
        else: hi = mid-1
    return -1

list = [1,2,3,4,5,7,8,9]
target = int(input("Enter element to search:"))
result = search(list, target)
if(search(list, target) != -1):
    print("Element found at index:",result)
else: print("Element not found")



