def check_for_word():
   
 word = "python"
 with open("practice.txt","r") as f:
    data = f.read()
    if(word in data):
        print("WORD FOUND")
    else:
        print("WORD NOT FOUND")
 return -1
print(check_for_word())

def check_for_line():        
 word = "python"
 data = True        
 line_no = 1
 with open("practice.txt") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(line_no)
            return
        line_no+=1

 return -1           
print(check_for_line())




    
  

  


