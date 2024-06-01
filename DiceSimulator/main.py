import random

class Dice:
    Dice_Number=0
    l1 = []
    def __init__(self):       
        try:
            self.Dice_Number= int(input("How many dices you want?"))
        except ValueError as E:
            print("Please enter a valid number")
           
    
    def Output(self):
        
        for i in range(self.Dice_Number):
            self.l1.append(random.randint(1,6))
            
        print(self.l1, end="")
        self.sum()
        
    def sum(self):
        sum=0
        for index,items in enumerate(self.l1):
            sum+=self.l1[index]
        print('\t sum =',sum)
User= Dice()
User.Output()