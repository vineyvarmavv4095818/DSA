def pip(n):
    if(n==0):
        return
    print(n,end=" ")
    pip(n-1)
    print(n,end=" ")
    pip(n-1)
    print(n,end=" ")

pip(3)