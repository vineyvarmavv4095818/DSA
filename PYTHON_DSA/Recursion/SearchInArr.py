def search(list, target, idx):
    if(idx == len(list)): return False
    if(list[idx] == target): return True

    return search(list, target, idx+1)

list = [1,2,3,4,6,7,8]
print(search(list, 5, 0))