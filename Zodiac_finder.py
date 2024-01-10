'''
	Find zodiac animal based on the year

'''

from tkinter import *
from tkinter import messagebox

class Zodiac_Animal():
    
    def __init__(self):
        
        # Create the main window
        self.main_window = Tk()
        self.main_window.title("Zodiac Animal Finder")
        
        # Size of the window
        self.main_window.geometry("350x200+700+200")
        
        # Create a frame to hold all the widgets
        self.displayFrame = Frame(self.main_window)
        self.displayFrame.grid(row= 0, column= 0, rowspan= 4, columnspan= 4)
        
        # Ceate widgets
        self.year_label = Label(self.displayFrame, text= "In what year were your born: ")
        self.year_entry = Entry(self.displayFrame, width= 15)
        
        #  Pack everything on the frame using grid
        self.year_label.grid(row= 1, column= 0, padx= 10, pady= 10)
        self.year_entry.grid(row= 1, column= 1, padx= 10, pady= 10)
        
        # Create the frame for buttons and the result amount
        self.resultFrame = Frame(self.main_window)
        self.resultFrame.grid(row= 4, column= 1, rowspan= 4, columnspan= 4)
        
        self.find_bttn = Button(self.resultFrame, text= "Find out",
                                     command= self.find_zodiac)
        self.zodiac_lbl = Label(self.resultFrame, text= "")
        
        # Pack all the widgets into the resultFrame
        self.find_bttn.grid(row= 4, column= 1, padx= 10, pady= 10)
        self.zodiac_lbl.grid(row= 5, column= 1, padx= 10, pady= 10)
        
                    
        # Start with the window event loop
        self.main_window.mainloop()
        
    
    def find_zodiac(self):
        
        try:
            year = int(self.year_entry.get())
            
            if year < 0:
                messagebox.showerror("ERROR", "You must enter a positive number.")
            else:
                if year % 12 == 0:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Monkey")
                elif year % 12 == 1:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Rooster")
                elif year % 12 == 2:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Dog")
                elif year % 12 == 3:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Pig")
                elif year % 12 == 4:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Rat")
                elif year % 12 == 5:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Ox")
                elif year % 12 == 6:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Tiger")
                elif year % 12 == 7:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Rabbit")
                elif year % 12 == 8:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Dragon")
                elif year % 12 == 9:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Snake")
                elif year % 12 == 10:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Horse")
                elif year % 12 == 11:
                    self.zodiac_lbl.config(text= "Your zodiac sign is a Sheep")
        except ValueError:
            messagebox.showerror("ERROR", "You must enter a valid year number")
     
                
if __name__ == "__main__":
    Zodiac_Animal()
        
