def subset(n, l, r, s, list):
    if(r==n):
        list.append(s)
        return
    
    if(l<n):
        subset(n, l+1, r, s+"(", list)
    
    if(r<l):
        subset(n, l, r+1, s+")", list)
    
def generate_Parenthesis(n):

    list = []
    subset(n, 0, 0, "", list)
    return list

print(generate_Parenthesis(3))