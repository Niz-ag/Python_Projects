import customtkinter as ctk

class IncomeTaxCalculator:
    def __init__(self) -> None:
        self.window= ctk.CTk()
        self.window.title("Income Tax Calculator")
        self.window.geometry("350x200")
        self.window.resizable(False,False)

        self.padding :dict = {"padx":20, "pady":10}

        #Income label
        self.income_label= ctk.CTkLabel(self.window,text="INCOME: ")
        self.income_label.grid(row=0,column=0,**self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0,column=1,**self.padding)
        
        #Regime Radio
        self.radioVar= ctk.IntVar(value=1)
        self.Select_Radio = ctk.CTkRadioButton(self.window,text="Old Tax Regime",value=0,variable=self.radioVar)
        self.Select_Radio.grid(row=1,column=0, **self.padding)
        self.Select_Radio = ctk.CTkRadioButton(self.window,text="New Tax Regime",value=1,variable=self.radioVar)
        self.Select_Radio.grid(row=1,column=1, **self.padding)

        #Result
        self.Result_label = ctk.CTkLabel(self.window,text="Tax Calculated: ")
        self.Result_label.grid(row=2,column=0,**self.padding)
        self.Result_entry = ctk.CTkEntry(self.window)
        self.Result_entry.grid(row=2,column=1,**self.padding)
        self.Result_entry.insert(0,"0")

        #calculate Button

        self.Calculate_button = ctk.CTkButton(self.window,text="Calculate",command=self.calculateTax)
        self.Calculate_button.grid(row=3,column=1,**self.padding)
        

    def run(self)->None:
        self.window.mainloop()

if __name__ == "__main__":
    itc = IncomeTaxCalculator()
    itc.run()