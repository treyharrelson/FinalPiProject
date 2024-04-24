from tkinter import *
import time
from tkinter import messagebox
from datetime import datetime
counter = 66600
running = False



class MainGUI(Frame):
    
    def __init__(self, master):
        super().__init__(master, bg = "#749CBB")
        self.master = master
        self.setupGUI()

    # timer = StringVar()
    # timer.set('00:00.00')
    
    def setupGUI(self):

        t1 = Label(self.master, text = "Workout One", anchor = N, fg = "white", bg = "#749CBB", \
              height = 1, width = 25, font = ("texgyreadventor-regular", 27)).place(x = 125, y = 0)

        b1 = Button(self.master, text = 'Play', anchor = N, fg = "white", bg = "#5B8C5D", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).place(x = 165, y = 225)
        
        t2 = Label(self.master, text = "00:00.00", anchor = N, fg = "black", bg = "white", \
              height = 1, width = 7, font = ("texgyreadventor-regular", 40)).place(x = 285, y = 135)
        
        b2 = Button(self.master, text = 'Stop', anchor = N, fg = "white", bg = "#9C4B60", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).place(x = 425, y = 225)
        
        b3 = Button(self.master, text = 'Reset', anchor = N, fg = "white", bg = "#748CBB", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 20)).place(x = 50, y = 400)
        
        b3 = Button(self.master, text = 'Next Workout', anchor = N, fg = "white", bg = "#9E6CA8", \
              height = 1, width = 11, font = ("texgyreadventor-regular", 20)).place(x = 550, y = 10)
        
    #     tt = Label(self.master, textvariable=MainGUI.timer, width = 8,  font = 'Helvetica 14').place(x=420, y=120)
        

    # # Define the function for the timer
    # def stop_watch(self):
    #     start_time = time.time()
    #     running = True
    #     while running:
    #         elapsed_time = time.time() - start_time
    #         minute, second = (elapsed_time // 60, elapsed_time % 60)
    #         second = round(second, 2)
    #         minute =  int(minute)
    #         MainGUI.timer.set(f"{minute}:{second}")

    #         # update the time
    #         root.update()
    #         time.sleep(.01)

######################## MAIN ###########################
root = Tk()
root.configure(bg="#749CBB")

# generate the GUI
p = MainGUI(root)
root.geometry("750x500")

# display the GUI and wait for user interaction
root.mainloop()
