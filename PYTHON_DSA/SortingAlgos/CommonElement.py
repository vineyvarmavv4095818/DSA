def find(a,b,ans):
    i, j = 0, 0
    a.sort()
    b.sort()

    while(i < len(a) and j < len(b)):
        if(a[i] == b[j]):
            ans.append(a[i])
            i =+ 1
            j += 1
        
        elif(a[i] < b[j]): i += 1
        else: j += 1

    return ans

a = [5,3,2,4]
b = [1,3,2,6]
ans = []
print(find(a,b,ans))