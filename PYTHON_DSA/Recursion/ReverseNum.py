def reverse(n, r):
    if(n==0):
        return r
    
    return reverse(n//10, r*10 + n%10)

n = 1675

print(reverse(n, 0))