count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    list = data.split(",")
    for val in list:
        if(int(val)%2==0):
            count+=1
    print(count)        
