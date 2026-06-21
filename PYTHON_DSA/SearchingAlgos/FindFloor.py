def find(list, tar):
    n = len(list)
    lo, hi, idx  = 0, n-1, -1

    while(lo<=hi):
        mid = (lo+hi)//2
        if(list[mid] > tar): hi = mid-1
        else:
            idx = mid
            lo = mid+1

    return list[idx]

list = [1,2,4,9,11,12,17]
print(find(list, 11))