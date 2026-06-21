def firstOcc(list, tar):
    lo, hi, idx = 0, len(list)-1, -1

    while(lo <= hi):
        mid = (lo + hi)//2

        if(list[mid] < tar): lo = mid+1
        elif(list[mid] > tar): hi = mid-1
        else:
            idx = mid
            hi  = mid-1
        
    return idx

def lastOcc(list, tar):
    lo, hi, idx2 = 0, len(list)-1, -1

    while(lo <= hi):
        mid = (lo + hi)//2

        if(list[mid] < tar): lo = mid+1
        elif(list[mid] > tar): hi = mid-1
        else:
            idx2 = mid
            lo = mid+1
        
    return idx2

list = [1,2,3,3,3,4,4,5,5,5,6,7]

print(firstOcc(list, 5))
print(lastOcc(list, 5))