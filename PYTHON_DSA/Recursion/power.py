# def pow(a, b):
#     if(b==0):
#         return 1
    
#     return a*pow(a, b-1)

# print(pow(4, 0))

def pow(a, b):
    if(b==0):
        return 1
    
    call = pow(a, b//2)
    
    if(b%2==0): return call * call
    else: return a * call * call

print(pow(3, 4))