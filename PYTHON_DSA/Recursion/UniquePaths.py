def uniquepaths(m, n):
    if(m==1 or n==1): return 1

    return uniquepaths(m-1, n) + uniquepaths(m, n-1)

print(uniquepaths(4,3))
