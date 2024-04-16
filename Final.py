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

    def setupGUI(self):

        t1 = Label(self.master, text = "Workout One", anchor = N, fg = "white", bg = "#749CBB", \
              height = 1, width = 25, font = ("texgyreadventor-regular", 27)).place(x = 125, y = 0)

        b1 = Button(self.master, text = 'Play', anchor = N, fg = "white", bg = "#748CBB", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).place(x = 295, y = 175)
        

######################## MAIN ###########################
root = Tk()
root.configure(bg="#749CBB")

# generate the GUI
p = MainGUI(root)
root.geometry("750x500")

# display the GUI and wait for user interaction
root.mainloop()