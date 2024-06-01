import string
import secrets

class Password_Generation:

    def __init__(self):

        self.Number_password:int =int(input("How many Passwords "))
        self.Length_password:int =int(input("What length of Password "))

        self.bool_symbols = input(" Symbols? Enter True or False ")
        self.bool_symbols :bool = True if self.bool_symbols == 'True' or "true" else False

        self.bool_upper =input(" Uppercase? Enter True or False ")
        self.bool_upper :bool = True if self.bool_upper == 'True' or 'true' else False
        

    def uppercase(self,password: str) -> bool:
        for char in password:
            if char.isupper():
                return True
        return False

    def symbols(self,password:str) -> bool:
        for char in password:
            if char in string.punctuation:
                return True
        return False

    def generate_password(self, length:int, symbol:bool, uppercase:bool) -> str:
        combination: str = string.ascii_lowercase + string.digits        
        if symbol:
            combination+= string.punctuation
        if uppercase:
            combination+= string.ascii_uppercase
            
        length_combination = len(combination)     

        new_password :str = ""
        for index in range(length):
            new_password+=combination[secrets.randbelow(length_combination)]
        
        return new_password
        
user = Password_Generation()
for i in range(user.Number_password):
    new_password :str = user.generate_password(user.Length_password,user.bool_symbols,user.bool_upper)
    print(new_password)