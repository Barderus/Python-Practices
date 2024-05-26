'''
	App that converts dollars -> cents
		cents -> dollars
'''

from tkinter import *
from tkinter import messagebox

class Money_Converter():
    
    QUARTERS = 25
    DIME = 10
    NICKELS = 5
    PENNY = 1
    
    BILL_1 = 1
    BILL_5 = 5
    BILL_10 = 10
    BILL_20 = 20
    BILL_50 = 50
    BILL_100 = 100
    
    def __init__(self):
        
        # Create the main window
        self.main_window = Tk()
        self.main_window.title("Money Converter")
        
        # Size of the window
        self.main_window.geometry("350x300+700+200")
        
        # Create a frame to hold all the widgets
        self.displayFrame = Frame(self.main_window)
        self.displayFrame.grid(row= 0, column= 0, rowspan= 4, columnspan= 4)
        
        # Radio button to see which way to convert
        self.var = DoubleVar()
        self.option1_buttn = Radiobutton(self.displayFrame, text= "Dollars to Cents", variable= self.var, value= 1)
        
        # Ceate widgets
        self.amount_label = Label(self.displayFrame, text= "Enter the amount of money: ")
        self.amount_entry = Entry(self.displayFrame, width= 15)
        
        #  Pack everything on the frame using grid
        self.option1_buttn.grid(row= 0, column= 0, padx= 10, pady= 10)
        self.amount_label.grid(row= 1, column= 0, padx= 10, pady= 10)
        self.amount_entry.grid(row= 1, column= 1, padx= 10, pady= 10)
        
        # Create the frame for buttons and the result amount
        self.resultFrame = Frame(self.main_window)
        self.resultFrame.grid(row= 4, column= 1, rowspan= 4, columnspan= 4)
        
        self.calculate_bttn = Button(self.resultFrame, text= "Calculate",
                                     command= self.calculate)
        self.result_list = Listbox(self.resultFrame, width= 20, height= 5)
        
        # Pack all the widgets into the resultFrame
        self.calculate_bttn.grid(row= 4, column= 1, padx= 10, pady= 10)
        self.result_list.grid(row= 5, column= 1, padx= 10, pady= 10)
        
                    
        # Start with the window event loop
        self.main_window.mainloop()
        
    
    def calculate(self):
        print(self.var.get())
        if self.var.get() == 1:
            self.dollar_to_cents()

            
        #self.result_list.delete(0, "end")
        
    def dollar_to_cents(self):
        
        self.result_list.delete(0, "end")
        try:
            
            # Make sure it is a positive number
            if float(self.amount_entry.get()) < 0:
                messagebox.showerror("ERROR", "The entered number must be positive.")
            
            else:    
                # Transforming the dollar amount into cents by multiplyer by 100
                cents_amnt = float(self.amount_entry.get()) * 100

                # Divide the cents into quarters and set  the remainder as cents
                quarts = int(cents_amnt) // self.QUARTERS
                cents_amnt = cents_amnt % self.QUARTERS
                
                # Divide the cents into dimes and set  the remainder as cents
                dime = int(cents_amnt) // self.DIME
                cents_amnt = cents_amnt % self.DIME

                # Divide the cents into nickels and set  the remainder as cents
                nickels = int(cents_amnt) // self.NICKELS
                cents_amnt = cents_amnt % self.NICKELS

                # Leftover cents are the pennies
                penny = int(cents_amnt)
                
                display_result = f"Quarters: {quarts}\nDime: {dime}\nNickels: {nickels}\nPenny: {penny}"
                
                result_lines = display_result.split("\n")
                for lines in result_lines:
                    self.result_list.insert("end", lines)
                    
        except ValueError:
            messagebox.showerror("ERROR", "The value entered must be a float number. For example: 7.35")
        
                
if __name__ == "__main__":
    Money_Converter()
        
