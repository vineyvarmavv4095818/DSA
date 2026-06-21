def focc(list, target, idx, count):
    #base case
    if(idx==len(list)):
        return -1

    if(target==list[idx]):
        count+=1
    
    if(count==2):
        return idx
    
    return focc(list, target, idx+1, count)

list = [1,2,4,3,5,3,4,7]
print(focc(list, 3, 0, 0))