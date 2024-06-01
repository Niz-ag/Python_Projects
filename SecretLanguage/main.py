import encoder
import decoder

User_Choice=input('''\t\t\t
Enter 'E' to Encode a sentence and Enter 'D' to Decode a sentence: ''')
if not (User_Choice =='E' or User_Choice =='D'):
    raise ValueError("Incorrect Input!")
Choice='Encode'
if User_Choice == 'D':
    Choice='Decode'
with open('input.txt','w') as f:
    f.write(input(f"Enter the sentence you wanna {Choice}\n"))

if User_Choice == 'E':
    encoder.encode()
elif User_Choice == 'D':
    decoder.decode()

        
if(User_Choice=='E'):
    with open("Encoded String.txt",'r') as f:
        print(f.readline())
else:
    with open("Decoded string.txt",'r') as f:
        print(f.readline())    