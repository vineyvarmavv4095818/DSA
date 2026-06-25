## Valid Parentheses

def check(s):

    st = []

    for i in s:

        if i=='(':
            st.append(i)
        else:
            if st==[]:
                return False

            st.pop()
    
    return len(st)==0

print(check("(()())"))