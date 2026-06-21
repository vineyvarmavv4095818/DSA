def find(n):
#     root = 0
#     for i in range(1,n+1):
#         if(i*i > n):
#             break

#         root = i

#     return root

# print(find(5))

    lo, hi = 1, n
    while(lo<=hi):
        mid = (lo+hi)//2

        if(mid*mid == n): return mid
        elif(mid*mid > n): hi = mid-1
        else: lo = mid+1

    return hi

print(find(26))