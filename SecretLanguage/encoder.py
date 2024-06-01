import random
import string
def encode():
    with open('input.txt','r') as f:
        S=f.readline()
        lst=S.split()
    
    
    output =""
    out=""
    def Grt3(inp):
    
        Len_S=len(inp)
        inp = inp[1:Len_S]+(inp[0])
        inp.replace(inp[0],"")    
       
        letters=string.ascii_lowercase + string.ascii_uppercase
        output= "".join(inp)

        for i in range(0,3):
            random_letter = random.choice(letters)
            output= random_letter+output
            random_letter = random.choice(letters)
            output= output+random_letter
        return output

    def lwr3(inp):
        lst2=[]
        for i in inp:
            lst2.append(i)
        lst2.reverse()    
        opt ="".join(lst2)
        return opt

   
    for index,items in enumerate(lst):  
       if len(items)>3:
           output= Grt3(items)      
       else:
           output=lwr3(items)         
       out= out + " " +output   
     
    with open('Encoded String.txt','w')as w:           
        w.write(out)
