def bs(list):
    n = len(list)

    for i in range(n):
        isSorted = True
        for k in range(n-1):
            if(list[k] > list[k+1]):
                isSorted = False
                break
        
        if(isSorted == True): break
        for j in range(0, n-i-1):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    
    return list

# list = [-1,3,5,7,6,0,1,3,4,-3,-2]
list = [1,2,3,4,5,6,7]
print(bs(list))