def search(list):
    n = len(list)
    lo, hi = 0, n-1
    while(lo<=hi):
        mid = (lo+hi)//2

        if(list[mid]>list[mid-1] and list[mid]>list[mid+1]):
            return mid
        elif(list[mid]>list[mid-1] and list[mid]<list[mid+1]):
            lo = mid+1
        else: hi = mid-1

list = [1,2,3,4,5,6,8,6,5,4,1,0]
print("Target found at index:",search(list))