import tkinter as tk
import time
from tkinter import messagebox
from datetime import datetime
counter = 66600
running = False

class Workout1:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        tk.Label(self.frame, text = "Workout One", anchor = "n", fg = "white", bg = "#749CBB", \
              height = 1, width = 25, font = ("texgyreadventor-regular", 27)).pack() #place(x = 125, y = 0)

        tk.Button(self.frame, text = 'Play', anchor = "n", fg = "white", bg = "#5B8C5D", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).pack() #place(x = 165, y = 225)
        
        tk.Label(self.frame, text = "00:00.00", anchor = "n", fg = "black", bg = "white", \
              height = 1, width = 7, font = ("texgyreadventor-regular", 40)).pack() #place(x = 285, y = 135)
        
        tk.Button(self.frame, text = 'Stop', anchor = "n", fg = "white", bg = "#9C4B60", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).pack() #place(x = 425, y = 225)
        
        tk.Button(self.frame, text = 'Reset', anchor = "n", fg = "white", bg = "#748CBB", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 20)).pack() #place(x = 50, y = 400)
        
        tk.Button(self.frame, text = 'Next Workout', anchor = "n", fg = "white", bg = "#9E6CA8", \
              height = 1, width = 11, font = ("texgyreadventor-regular", 20), command=self.make_page_2).pack() #place(x = 555, y = 10)
        
        tk.Label(self.frame, text='Weight Lifted (lbs):', bd = 6, font = ("texgyreadventor-regular", 10)).pack() #place(x= 10, y = 10)
        
        # entry = tk.Entry(self.frame, bd = 5, bg = 'white', font = 'Helvetica 14',  fg = 'black', width = 7, text = 'Weight Lifted',
        #             anchor = "center",).place(x = 140, y = 10)
        
        self.page_2 = Workout2(master=self.root, app=self)
        self.page_3 = Workout3(master=self.root, app=self)
    
    def main_page(self):
        self.frame.pack()
    
    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()

    # timer = StringVar()
    # timer.set('00:00.00')
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
class Workout2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
    
        t1 = tk.Label(self.frame, text = "Workout Two", anchor = "n", fg = "white", bg = "#749CBB", \
              height = 1, width = 25, font = ("texgyreadventor-regular", 27)).pack() #place(x = 125, y = 0)
        
        b1 = tk.Button(self.frame, text = 'Play', anchor = "n", fg = "white", bg = "#5B8C5D", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).pack() #place(x = 165, y = 225)
        
        timer = tk.Label(self.frame, text = "00:00.00", anchor = "n", fg = "black", bg = "white", \
              height = 1, width = 7, font = ("texgyreadventor-regular", 40)).pack() #place(x = 285, y = 135)
        
        b2 = tk.Button(self.frame, text = 'Stop', anchor = "n", fg = "white", bg = "#9C4B60", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).pack() #place(x = 425, y = 225)
        
        b3 = tk.Button(self.frame, text = 'Reset', anchor = "n", fg = "white", bg = "#748CBB", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 20)).pack() #place(x = 50, y = 400)
        
        b4 = tk.Button(self.frame, text = 'Next Workout', anchor = "n", fg = "white", bg = "#9E6CA8", \
              height = 1, width = 11, font = ("texgyreadventor-regular", 20), command=self.make_page_3).pack() #place(x = 555, y = 10)
        
        t2 = tk.Label(self.frame, text='Weight Lifted (lbs):', bd = 6, font = ("texgyreadventor-regular", 10)).pack() #place(x= 10, y = 10)
        # entry = tk.Entry(self.frame, bd = 5, bg = 'white', font = 'Helvetica 14',  fg = 'black', width = 7, text = 'Weight Lifted',
        #             anchor = "center",).place(x = 140, y = 10)
    
    def start_page(self):
        self.frame.pack()
    
    def make_page_3(self):
        self.frame.pack_forget()
        self.app.page_3.start_page()

class Workout3:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        
        t1 = tk.Label(self.frame, text = "Workout Three", anchor = "n", fg = "white", bg = "#749CBB", \
              height = 1, width = 25, font = ("texgyreadventor-regular", 27)).pack() #place(x = 125, y = 0)
        
        b1 = tk.Button(self.frame, text = 'Play', anchor = "n", fg = "white", bg = "#5B8C5D", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).pack() #place(x = 165, y = 225)
        
        timer = tk.Label(self.frame, text = "00:00.00", anchor = "n", fg = "black", bg = "white", \
              height = 1, width = 7, font = ("texgyreadventor-regular", 40)).pack() #place(x = 285, y = 135)
        
        b2 = tk.Button(self.frame, text = 'Stop', anchor = "n", fg = "white", bg = "#9C4B60", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 50)).pack() #place(x = 425, y = 225)
        
        b3 = tk.Button(self.frame, text = 'Reset', anchor = "n", fg = "white", bg = "#748CBB", \
              height = 1, width = 5, font = ("texgyreadventor-regular", 20)).pack() #place(x = 50, y = 400)
        
        b4 = tk.Button(self.frame, text = 'Next Workout', anchor = "n", fg = "white", bg = "#9E6CA8", \
              height = 1, width = 11, font = ("texgyreadventor-regular", 20), command=self.go_back).pack() #place(x = 555, y = 10)
        
        t2 = tk.Label(self.frame, text='Weight Lifted (lbs):', bd = 6, font = ("texgyreadventor-regular", 10)).pack() #place(x= 10, y = 10)
        #entry = tk.Entry(self.frame, bd = 5, bg = 'white', font = 'Helvetica 14',  fg = 'black', width = 7, text = 'Weight Lifted',
        #            anchor = "center",).place(x = 140, y = 10)
    
    def start_page(self):
        self.frame.pack()
    
    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

######################## MAIN ###########################
if __name__ == '__main__':
    root = tk.Tk()
    # root.configure(bg="#749CBB")
    # root.geometry("750x500")
    
    # generate the GUI
    app = Workout1(root)
    # display the GUI 
    root.mainloop()