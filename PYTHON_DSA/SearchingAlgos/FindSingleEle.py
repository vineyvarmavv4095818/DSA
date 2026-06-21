def singleEle(list):
    n = len(list)

    if(n==1): return list[0]
    if(list[0] != list[1]): return list[0]
    if(list[n-1] != list[n-2]): return list[n-1]

    lo, hi = 0, n-1

    while(lo <= hi):
        mid = (lo+hi)//2

        if(list[mid] != list[mid-1] and list[mid] != list[mid+1]): return list[mid]

        f, s = mid, mid

        if(list[mid] == list[mid-1]):
            f = mid-1
        else: s = mid+1

        leftCount = f - lo
        if(leftCount%2==0): lo = s+1
        else: hi = f-1

    return -1


list = [1,1,2,2,3,3,4,4,5,6,6]
result = singleEle(list)
print(result)