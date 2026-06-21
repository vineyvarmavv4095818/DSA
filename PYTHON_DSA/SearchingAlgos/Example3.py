def find(list, k):
    n = len(list)
    lo, hi = 0, len(list)-1

    while(lo <= hi):
        mid = (lo+hi)//2
        corretNo = mid+1
        missingCount = list[mid] - corretNo

        if(missingCount >= k): hi = mid-1
        else: lo = mid+1

    return lo+k

list = [1,2,4,6,8,10]
print(find(list, 2))