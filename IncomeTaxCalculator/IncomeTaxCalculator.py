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
                

        #Result
        self.Result_label = ctk.CTkLabel(self.window,text="Tax Calculated: ")
        self.Result_label.grid(row=2,column=0,**self.padding)
        self.Result_entry = ctk.CTkEntry(self.window)
        self.Result_entry.grid(row=2,column=1,**self.padding)
        self.Result_entry.insert(0,"0")

        #calculate Button

        self.Calculate_button = ctk.CTkButton(self.window,text="Calculate",command=self.returnCalculateTax)
        self.Calculate_button.grid(row=3,column=1,**self.padding)
        
    def update_result(self,text:str):
        self.Result_entry.delete(0,ctk.END)
        self.Result_entry.insert(0,text)
    

    def calculateTax(self,income:float):
        taxable_income= income        
        if(income<300000):
            tax=0.0            
        elif(income<700000):
            taxable_income= income-300000
            tax= taxable_income*0.05
        elif(income<1000000):
            taxable_income= income-700000
            tax= taxable_income*0.1 + 20000
        elif(income<1200000):
            taxable_income = income-1000000
            tax = taxable_income*0.15 +20000+30000
        elif(income<1500000):
            taxable_income= income-1200000
            tax= taxable_income*0.2 +20000+30000+45000
        else:
            taxable_income= income-1500000
            tax= taxable_income*0.3 + 20000+30000+45000+60000      
        
        return tax

    def returnCalculateTax(self):
        try:
            income:float = float(self.income_entry.get())
            tax_result = self.calculateTax(income)
            self.update_result(f"{tax_result:,.2f}")
        except ValueError:
            self.update_result("Invalid Results")

    def run(self)->None:
        self.window.mainloop()

if __name__ == "__main__":
    itc = IncomeTaxCalculator()
    itc.run()