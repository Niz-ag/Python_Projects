import os
real_path = os.path.dirname(os.path.realpath(__file__))

def opener() ->list[str]:
    with open(f"{real_path}/passwords.txt","r") as f:
        reader :list[str]=f.read().splitlines()
    return reader

def insertion() ->str:
    user_input:str=input("Enter Your Password")
    return user_input

def main()->None:
    user = insertion()
    data:list[str]= opener()

    for (index,value) in enumerate(data,start=1):
        if(value==user):
            print(f"{value} ❌ (#{index})")
            return
    print(f"{user} ✅ Unique")

if __name__ == '__main__':
    main()