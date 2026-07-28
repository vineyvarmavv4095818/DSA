# TC = O(nlog n) + O(mlog m) + O(m)
# n = len(g)
# m = len(s)

def asign(g,s):
    count = 0
    g.sort()
    s.sort()
    left = 0
    right = 0

    while left<len(g) and right<len(s):
        if g[left] <= s[right]:
            count += 1
            left += 1
        right +=1

    return count

g = [6,8,2,1,4]
s = [3,4,7,2,1,2,8]

print(asign(g, s))