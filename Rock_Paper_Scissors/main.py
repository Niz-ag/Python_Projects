import random

def game(AI,Player):
    if AI == Player:
        return None
    elif AI == 'R':
        if Player== 'S':
            return False
        elif Player == 'P':
            return True
    
    elif AI == 'P':
        if Player== 'R':
            return False
        elif Player == 'S':
            return True

    elif AI == 'S':
        if Player== 'P':
            return False
        elif Player == 'R':
            return True
    


print("Ai's Turn: Rock(R) Paper(P) Scissors(S)?\n")
RandNo = random.randint(1,3)
if RandNo == 1:
    AI = 'R'
elif RandNo == 2:
    AI = 'P'
elif RandNo == 3:
    AI = 'S'
Player = input("YourTurn: Rock(R) Paper(P) Scissors(S)?\n")
print("AI Chose", AI)
print("You Chose", Player)
Out = game(AI,Player)
if Out== None:
    print("\t*Tied*")
elif Out:
    print("\t*You WON*")
else :
    print("\t*You Lose*")