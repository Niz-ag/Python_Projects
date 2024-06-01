from english_words import get_english_words_set
import random
web2lowerset = get_english_words_set(['web2'], lower=True)

class Hangman:

    lives: int =3

    def Rand(self):
        return random.choice(list(web2lowerset))
    
    def __init__(self) -> None:
        Name: str= input("What is your name\n")
        print(f"\n\nHello {Name}, my Greetings!\n You are in the Hangman! \n\tYou have 3 lives!\n\tUse them wisely.")

    def Input(self): 
        return input("\nMake Your Guess: ")
    
    def Process(self) -> None:
        Guess : list=[]
        Randome:str = self.Rand()
        # print (Randome)
      
        for index in Randome:
            Guess.append("_")
            
        guess:str= ""
        while True:
            guess:str= ""
            for index in Guess:
                guess= guess+ index
                
            if(self.lives==0):
                print(f"\n\n!!!! \t\t You Lose \t\t!!!!\n \tThe word was:{Randome} ")
                break

            if(Randome== guess):
                print(f"\n\n!!!! \t\t You Won \t\t!!!! \n \t\t Remaining Lives: {self.lives}")
                break    

            print(f"Word {guess}") 

            Chk :str = self.Input()
            flag: int =0
            i: int=0
                        
            
            for index in Randome:                
                
                if Chk == Randome[i]:
                    Guess[i]=Chk
                    flag+=1                   
                i+=1
               

            if flag ==0:
                self.lives-=1
                print(f"\nYou made the wrong guess \n Remaining Lives: {self.lives} ")

            else:
                print("\nRight on!")

User = Hangman()
User.Process()