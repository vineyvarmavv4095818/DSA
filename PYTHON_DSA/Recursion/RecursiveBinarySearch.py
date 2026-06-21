def binaryS(list, lo, hi, target):
    if(lo > hi):
        return -1
    
    mid = (lo+hi)//2

    if(target==list[mid]):
        return mid
    
    if(target > list[mid]):
        return binaryS(list, mid+1, hi, target)
    
    return binaryS(list, lo, mid-1, target)

list = [1,2,3,4,5,6,7,8,9]

result = binaryS(list, 0, len(list)-1, 2)

if(result != -1):
    print("found at index:",result)
else: print("not found")