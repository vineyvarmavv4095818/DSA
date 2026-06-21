def neg(list):
    n = len(list)
    lo, hi, negcount = 0, n-1, 0

    while(lo <= hi):
        mid = (lo + hi)//2
        if(list[mid] >= 0): hi = mid-1
        else: lo = mid+1
        negcount = lo

    return negcount

def pos(list):
    n = len(list)
    lo, hi, poscount = 0, len(list)-1, 0

    while(lo <= hi):
        mid = (lo + hi)//2
        if(list[mid] <= 0): lo = mid+1
        else: hi = mid-1
        poscount = n-1-hi

    return poscount

list = [-1,-2,-3,-5,0,0,0,1,2,3]

print("Count of negative integers:",neg(list))
print("Count of positive integers:",pos(list))