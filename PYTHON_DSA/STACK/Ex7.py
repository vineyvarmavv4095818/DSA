## Insert at Bottom

def insert(st, x):

    if st==[]:
        st.append(x)
        return
    
    y = st.pop()

    insert(st, x)

    st.append(y)


stack = [1,2,3,4]

insert(stack, 10)

print(stack)