'''
	Calculate tips GUI app
        Needs to add try-catch
'''
from tkinter import *

class Tips_GUI():
    
    def __init__(self):
        
        # Create the main window
        self.main_window = Tk()
        self.main_window.title("Tip Calculator")
        
        # Size of the window
        self.main_window.geometry("500x200+700+200")
        
        # Create a frame to add content
        self.calcFrame = Frame(self.main_window, padx= 20, pady= 10)
        self.calcFrame.grid(row= 1, column= 1, columnspan= 5, rowspan= 5)
        
        # Create a label
        self.total_label = Label(self.calcFrame, text= "Enter the total value of the purchase: ")
        self.total_entry = Entry(self.calcFrame, width= 15)
        
        # Create radio buttons to choose % amount
        self.var = DoubleVar()
        self.option1_buttn = Radiobutton(self.calcFrame, text= "10 %", variable= self.var, value= 0.1)
        self.option2_buttn = Radiobutton(self.calcFrame, text= "15 %", variable= self.var, value= 0.15)
        self.option3_buttn = Radiobutton(self.calcFrame, text= "20 %", variable= self.var, value= 0.2)
        self.option4_buttn = Radiobutton(self.calcFrame, text= "25%", variable= self.var, value= 0.25)
        
        # Create the button to calculate the tip amount
        self.calc_bttn = Button(self.calcFrame, text= "Calculate", command= self.calc_tip)
        self.display_label = Label(self.calcFrame)
        
        # Pack everything in the frame using grid
        self.total_label.grid(row=1, column=1, padx= 10, pady= 10)
        self.total_entry.grid(row= 1, column= 2)
        self.option1_buttn.grid(row= 2, column=1)
        self.option2_buttn.grid(row= 2, column=2)
        self.option3_buttn.grid(row= 2, column=3)
        self.option4_buttn.grid(row= 2, column=4)
        self.calc_bttn.grid(row= 3, column= 2, padx= 10, pady= 10)
        self.display_label.grid(row= 4, column= 2, padx= 10, pady= 10)
        
        
        # Start with the window event loop
        self.main_window.mainloop()
    
    def calc_tip(self):
        # Calculate the tip to be given by multiplying the tip choice by the the total value from the entry. 
        tip_amnt = float(self.var.get()) * float(self.total_entry.get())
        # Calculate the total to pay by adding the tip to the total price of goods
        ttl_pay = tip_amnt + float(self.total_entry.get())
        text = f"The tip amount is: ${tip_amnt}\n Total to pay: ${ttl_pay}"
        # Change the values of display_label to text
        self.display_label.config(text = text)
        
        
if __name__ == "__main__":
    Tips_GUI()

