'''
    Timer application
'''

from tkinter import *
#from playsound import playsound
import time
from tkinter import messagebox

class Timer():
    
    def __init__(self):
        
        # Create the main window
        self.main_window = Tk()
        self.main_window.title("Timer")
        
        # Size of the window
        self.main_window.geometry("400x450+500+100")
        self.main_window.config(bg= "Black")
           
        # Create header label Timer
        self.header_lbl = Label(self.main_window, text= "Timer", font= "arial 30 bold", bg= "#000", fg="#ea3548")
        self.header_lbl.pack(pady=10)
        
        # Create label for the current to display the current
        self.current_lbl = Label(self.main_window, text= "Current time: ", font = "arial 15 bold", bg= "papaya whip")
        self.current_lbl.place(x=65, y = 70)
        
        self.clock_time = time.strftime("%H:%M:%S %p")

        self.current_time_lbl = Label(self.main_window, text= self.clock_time, font = "arial 15 bold", fg= "#000", bg = "#fff")
        self.current_time_lbl.place(x = 200, y = 70)
        
        # Create entry and label for hour           
        self.hours = StringVar()
        self.hours_entry = Entry(self.main_window, textvariable= self.hours, width=2, font= "arial 50", bg= "#000", fg= "#fff", bd= 0)
        self.hours_entry.place(x= 30, y= 155)
        self.hours.set("00")
        
        self.hours_label = Label(self.main_window, text= "hours", font= "arial 12", bg= "#000", fg= "#fff")
        self.hours_label.place(x= 105, y= 200)
        
        # Create entry and label for minutes
        self.minutes = StringVar()
        self.minutes_entry = Entry(self.main_window, textvariable= self.minutes, width=2, font= "arial 50", bg= "#000", fg= "#fff", bd= 0)
        self.minutes_entry.place(x= 150, y= 155)
        self.minutes.set("00")

        self.minutes_label = Label(self.main_window, text= "min", font= "arial 12", bg= "#000", fg= "#fff")
        self.minutes_label.place(x= 225, y= 200)
        
        # Create entry and label for seconds
        self.seconds = StringVar()
        self.seconds_entry = Entry(self.main_window, textvariable= self.seconds, width=2, font= "arial 50", bg= "#000", fg= "#fff", bd= 0)
        self.seconds_entry.place(x= 270, y= 155)
        self.seconds.set("00")

        self.seconds_label = Label(self.main_window, text= "sec", font= "arial 12", bg= "#000", fg= "#fff")
        self.seconds_label.place(x= 345, y= 200)
        
        # Create the start button
        self.start_bttn = Button(self.main_window, text= "Start", bg= "#ea3548", bd= 0, fg= "#fff", width= 20, height= 2, font= "arial 10 bold", command= self.timer)
        self.start_bttn.pack(padx= 5, pady= 40, side= BOTTOM)
        
        # Create the stop button
        self.stop_bttn = Button(self.main_window, text= "Stop", bg= "#ea3548", bd= 0, fg = "#fff", width= 20, height= 2, font= "arial 10 bold", command= self.stop)
        self.stop_bttn.pack(padx= 5, pady= 40, side= LEFT)
        
        # Create the reset button
        self.reset_bttn = Button(self.main_window, text= "Reset", bg= "#ea3548", bd= 0, fg = "#fff", width= 20, height= 2, font= "arial 10 bold", command= self.reset)
        self.reset_bttn.pack(padx= 5, pady= 40, side= LEFT)
        
        # Start with the window event loop
        self.main_window.mainloop()
        
    
    def timer(self):
        times = int(self.hours.get()) * 3600 + int(self.minutes.get()) * 60 + int(self.seconds.get())
        self.timer_run = True
        self.update_timer(times)
        
                
    def update_timer(self, remaining_time):
        
        if remaining_time >= 0 and self.timer_run:
            min = remaining_time // 60
            sec = remaining_time % 60
            hour = min // 60
            min = min % 60
            
            self.seconds.set("{:02}".format(sec))
            self.minutes.set("{:02}".format(min))
            self.hours.set("{:02}".format(hour))
            
            self.main_window.update()
            self.main_window.after(1000, self.update_timer, remaining_time - 1)
            
        elif remaining_time < 0 and self.timer_run:
            messagebox.showwarning("WARNING", "Time's up!")
            self.seconds.set("00")
            self.minutes.set("00")
            self.hours.set("00")
            
    
    def stop(self):
        self.timer_run = False
        
    def reset(self):
        self.stop()
        
        self.hours.set("00")
        self.minutes.set("00")
        self.seconds.set("00")
        
                 
        
        
                
if __name__ == "__main__":
    Timer()
        
