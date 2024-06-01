import random
import os
real_path = os.path.dirname(os.path.realpath(__file__))
print(real_path)

randNumber = random.randint(1, 100)

class Check:    

    @staticmethod
    def Higher():
        print(f"\tEnter Smaller number.")
        
    @staticmethod
    def Lower():
        print(f"\tEnter Larger number.")
            
    def Correct(self,UserGuess):
        print(f"\t\tYOU WON!! \n\tYou took {UserGuess} guess to arrive at this number.")        

class EnterNum(Check):
    UserNumber=None
    try:
        def __init__(self):
            self.username :str= input("Please Enter your name!")
            self.UserNumber = int(input("Enter the number.\n"))
            self.UserGuess=1

        def nextInput(self):
            self.UserNumber = int(input("Enter the number.\n"))
            self.UserGuess+=1
    except ValueError as E:
        print('Please Enter a valid Number')


User= EnterNum()
while(randNumber!=User.UserNumber):
    if(User.UserNumber>randNumber):
       User.Higher()
       User.nextInput()
    elif(User.UserNumber<randNumber):
      User.Lower()
      User.nextInput()
UserGuess= User.UserGuess
User.Correct(UserGuess)
try:
    with open(f'{real_path}/hiscore.txt','r') as f:
        hiscore = int(f.readline())
        hiname = f.readline()
except:
    with open(f'{real_path}/hiscore.txt','w+') as f:
        f.write("999\n default")
        hiscore = int(f.readline())
        hiname = f.readline()
with open(f'{real_path}/hiscore.txt','w+') as f:
    if UserGuess<hiscore:
        f.write(str(UserGuess))
        f.write(str("\n" + User.username))
    else:       
        f.write(str(hiscore))
        f.write(str(f"\n{hiname}"))
        f.seek(0)
        print(f"\tHiscore is {f.readline()} \tby {f.readline()}")
