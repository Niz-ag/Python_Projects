def decode():
    with open('input.txt','r') as f:
        S=f.readline()
        lst=S.split()  
    output =""
    out=""
    
    def Grt3(inp):
        Len_S=len(inp)
        inp=inp.replace(inp[:3],"")
        inp=inp.replace(inp[-3:],"")
        Len_S=len(inp)
            
        f_l=inp[Len_S-1]
        inp=f_l+inp[:Len_S-1] 
        return inp
    
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
        
    with open('Decoded string.txt','w')as w:   
        data= w.write(out)
