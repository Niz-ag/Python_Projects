import requests
from typing import Final
import customtkinter as ctk
class link_shortener():
    def __init__(self)->None:    

        self.API_KEY:Final[str]="4f3e0dc5e86967848752f4e4855a122ab97f3"
        self.Base_URL:Final[str]= "https://cutt.ly/api/api.php"

        self.window=ctk.CTk()
        self.window.title("Link shortener")
        self.window.geometry("400x200")
        self.window.resizable(False,False)
    
        self.padding:dict={"padx":20,"pady":10}    

        #Input
        self.UI_Label = ctk.CTkLabel(self.window,text="Your OLD link:")
        self.UI_Label.grid(row=0,column=0,**self.padding)
        self.UI_Entry = ctk.CTkEntry(self.window,width=200)
        self.UI_Entry.grid(row=0,column=1,**self.padding)

        #Output
        self.OT_Label = ctk.CTkLabel(self.window,text="Your NEW link")
        self.OT_Label.grid(row=1,column=0,**self.padding)
        self.OT_Entry = ctk.CTkEntry(self.window,width=200)
        self.OT_Entry.grid(row=1,column=1,**self.padding)
        self.OT_Entry.insert(0,"www.google.com")
        self.OT_Entry.configure(state="disabled")

        self.Calculate_button = ctk.CTkButton(self.window,text="Shorten",command=lambda: self.shorten_link(self.UI_Entry.get()))
        self.Calculate_button.grid(row=2,column=1,**self.padding)
        
    def update_result(self,text:str):
        self.OT_Entry.configure(state="normal")
        self.OT_Entry.delete(0,ctk.END)
        self.OT_Entry.insert(0,text)
        self.OT_Entry.configure(state="disabled")

        

    
         
    
    def shorten_link(self,User_link)->None:
        payload:dict={"key":self.API_KEY,"short":User_link}
        request= requests.get(self.Base_URL, params=payload)
        data:dict = request.json()
    
        if url_data:=data.get('url'):
            if url_data['status']==7 :
                short=url_data['shortLink']
                self.update_result(f"{short}")
                print(short)
            else:
                self.update_result(f'{url_data["status"]}')

                print(url_data["status"]) 
           

    def run(self)->None:
        self.window.mainloop()

if __name__ == "__main__":     
    LS=link_shortener()
    LS.run()