## Delete Middle Element

def remove(st, k):

    if k==0:
        st.pop()
        return
    
    x = st.pop()

    remove(st, k-1)

    st.append(x)

stack = [1,2,3,4,5,2,6,4]

remove(stack, len(stack)//2)

print(stack)