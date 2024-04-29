import tkinter as tk
import time
from tkinter import messagebox
from datetime import datetime
# from stopwatch import run_stop_watch
counter = 66600
running = False

class Workout1:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root, bg = "#749CBB")
        self.frame.pack()
        self.setupGUI()
        self.page_2 = Workout2(master=self.root, app=self)
        self.page_3 = Workout3(master=self.root, app=self)
    
    # Initializes all widgets on the page
    # Sets up 3 different sections on the page using tk.Frame
    def setupGUI(self):
        
    # Frame 1 setup
        self.frame1 = tk.Frame(self.frame, bg = "#749CBB")
        
        t1 = tk.Label(self.frame1, text = "Workout One", fg = "white",
                      bg = "#749CBB", font = ("texgyreadventor-regular",30))
        t1.grid(row=0, column=0, pady=(10,0), sticky="")
        
    # Frame 2 setup
        self.frame2 = tk.Frame(self.frame, bg = "#749CBB")
        
        t3 = tk.Label(self.frame2, text = 'Weight Lifted (lbs):', font = ("texgyreadventor-regular", 10))
        t3.grid(row=0, column=0, padx=(10,0), sticky="")
        
        entry = tk.Entry(self.frame2, bd = 5, width= 4, bg = 'white', font = ("texgyreadventor-regular"), 
                         fg = 'black', text = 'Weight Lifted',)
        entry.grid(row=0, column=1, padx=(5,345), sticky="")
        
        b4 = tk.Button(self.frame2, text = 'Next Workout', fg = "white", bg = "#9E6CA8",
                       font = ("texgyreadventor-regular", 20), command=self.make_page_2)
        b4.grid(row=0, column=2, padx=(0,10), sticky="")
        
        self.displayed_time = tk.StringVar()
        timer = tk.Label(self.frame2, textvariable = self.displayed_time, fg = "black", bg = "white",
                         font = ("texgyreadventor-regular", 40))
        self.displayed_time.set('00:00.00')
        timer.grid(row=1, column=0, columnspan=3, pady=(30,20), sticky="")
        
    # Frame 3 setup
        self.frame3 = tk.Frame(self.frame, bg = "#749CBB")
        
        b1 = tk.Button(self.frame3, text = 'Play', fg = "white", bg = "#5B8C5D",
                       font = ("texgyreadventor-regular", 50), command = self.run_stop_watch)
        b1.grid(row=0, column=0, padx=30, sticky="")
        
        b2 = tk.Button(self.frame3, text = 'Stop', fg = "white", bg = "#9C4B60",
                       font = ("texgyreadventor-regular", 50), command = self.stop_stop_watch)
        b2.grid(row=0, column=1, padx=30, sticky="")
        
        b3 = tk.Button(self.frame3, text = 'Reset', fg = "white", bg = "#748CBB",
                       font = ("texgyreadventor-regular", 20), command = self.reset_stop_watch)
        b3.grid(row=1, column=1, pady=(30,10), sticky="")

        # pack each section then pack the frame as a whole
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
    
    def main_page(self):
        self.frame.pack()
    
    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()

    
    # Define the function for the timer
    def run_stop_watch(self):
        start_time = time.time()
        global running; running = True

        while running:
            elapsed_time = time.time() - start_time
            minute, second = (elapsed_time // 60, elapsed_time % 60)
            second = round(second, 2)
            minute =  int(minute)

            self.displayed_time.set(f"{minute}:{second}")

            # update the time
            self.root.update()
            time.sleep(.01)

    def stop_stop_watch(self):
        global running; running = False

    def reset_stop_watch(self):
        self.displayed_time.set('00:00.00')

class Workout2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, bg = "#749CBB")
        self.setupGUI()
    
    # Initializes all widgets on the page
    # Sets up 3 different sections on the page using tk.Frame
    def setupGUI(self):
        
    # Frame 1 setup
        self.frame1 = tk.Frame(self.frame, bg = "#749CBB")
        
        t1 = tk.Label(self.frame1, text = "Workout Two", fg = "white",
                      bg = "#749CBB", font = ("texgyreadventor-regular",30))
        t1.grid(row=0, column=0, pady=(10,0), sticky="")
        
    # Frame 2 setup
        self.frame2 = tk.Frame(self.frame, bg = "#749CBB")
        
        t3 = tk.Label(self.frame2, text = 'Weight Lifted (lbs):', font = ("texgyreadventor-regular", 10))
        t3.grid(row=0, column=0, padx=(10,0), sticky="")
        
        entry = tk.Entry(self.frame2, bd = 5, width= 4, bg = 'white', font = ("texgyreadventor-regular"), 
                         fg = 'black', text = 'Weight Lifted',)
        entry.grid(row=0, column=1, padx=(5,345), sticky="")
        
        b4 = tk.Button(self.frame2, text = 'Next Workout', fg = "white", bg = "#9E6CA8",
                       font = ("texgyreadventor-regular", 20), command=self.make_page_3)
        b4.grid(row=0, column=2, padx=(0,10), sticky="")
        
        self.displayed_time = tk.StringVar()
        timer = tk.Label(self.frame2, textvariable = self.displayed_time, fg = "black", bg = "white",
                         font = ("texgyreadventor-regular", 40))
        self.displayed_time.set('00:00.00')
        
        timer.grid(row=1, column=0, columnspan=3, pady=(30,20), sticky="")
        
    # Frame 3 setup
        self.frame3 = tk.Frame(self.frame, bg = "#749CBB")
        
        b1 = tk.Button(self.frame3, text = 'Play', fg = "white", bg = "#5B8C5D",
                       font = ("texgyreadventor-regular", 50), command = self.run_stop_watch)
        b1.grid(row=0, column=0, padx=30, sticky="")
        
        b2 = tk.Button(self.frame3, text = 'Stop', fg = "white", bg = "#9C4B60",
                       font = ("texgyreadventor-regular", 50), command = self.stop_stop_watch)
        b2.grid(row=0, column=1, padx=30, sticky="")
        
        b3 = tk.Button(self.frame3, text = 'Reset', fg = "white", bg = "#748CBB",
                       font = ("texgyreadventor-regular", 20), command = self.reset_stop_watch)
        b3.grid(row=1, column=1, pady=(30,10), sticky="")

        # pack each section then pack the frame as a whole
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
    
    def start_page(self):
        self.frame.pack()
    
    def make_page_3(self):
        self.frame.pack_forget()
        self.app.page_3.start_page()

    def run_stop_watch(self):
        start_time = time.time()
        global running; running = True

        while running:
            elapsed_time = time.time() - start_time
            minute, second = (elapsed_time // 60, elapsed_time % 60)
            second = round(second, 2)
            minute =  int(minute)

            self.displayed_time.set(f"{minute}:{second}")

            # update the time
            self.master.update()
            time.sleep(.01)

    def stop_stop_watch(self):
        global running; running = False

    def reset_stop_watch(self):
        self.displayed_time.set('00:00.00')

class Workout3:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, bg = "#749CBB")
        self.setupGUI()
        
    # Initializes all widgets on the page
    # Sets up 3 different sections on the page using tk.Frame
    def setupGUI(self):
        
    # Frame 1 setup
        self.frame1 = tk.Frame(self.frame, bg = "#749CBB")
        
        t1 = tk.Label(self.frame1, text = "Workout Three", fg = "white",
                      bg = "#749CBB", font = ("texgyreadventor-regular",30))
        t1.grid(row=0, column=0, pady=(10,0), sticky="")
        
    # Frame 2 setup
        self.frame2 = tk.Frame(self.frame, bg = "#749CBB")
        
        t3 = tk.Label(self.frame2, text = 'Weight Lifted (lbs):', font = ("texgyreadventor-regular", 10))
        t3.grid(row=0, column=0, padx=(10,0), sticky="")
        
        entry = tk.Entry(self.frame2, bd = 5, width= 4, bg = 'white', font = ("texgyreadventor-regular"), 
                         fg = 'black', text = 'Weight Lifted',)
        entry.grid(row=0, column=1, padx=(5,345), sticky="")
        
        b4 = tk.Button(self.frame2, text = 'Next Workout', fg = "white", bg = "#9E6CA8",
                       font = ("texgyreadventor-regular", 20), command=self.go_back)
        b4.grid(row=0, column=2, padx=(0,10), sticky="")
        
        self.displayed_time = tk.StringVar()
        timer = tk.Label(self.frame2, textvariable = self.displayed_time, fg = "black", bg = "white",
                         font = ("texgyreadventor-regular", 40))
        self.displayed_time.set('00:00.00')
        timer.grid(row=1, column=0, columnspan=3, pady=(30,20), sticky="")
        
    # Frame 3 setup
        self.frame3 = tk.Frame(self.frame, bg = "#749CBB")
        
        b1 = tk.Button(self.frame3, text = 'Play', fg = "white", bg = "#5B8C5D",
                       font = ("texgyreadventor-regular", 50), command = self.run_stop_watch)
        b1.grid(row=0, column=0, padx=30, sticky="")
        
        b2 = tk.Button(self.frame3, text = 'Stop', fg = "white", bg = "#9C4B60",
                       font = ("texgyreadventor-regular", 50), command = self.stop_stop_watch)
        b2.grid(row=0, column=1, padx=30, sticky="")
        
        b3 = tk.Button(self.frame3, text = 'Reset', fg = "white", bg = "#748CBB",
                       font = ("texgyreadventor-regular", 20), command = self.reset_stop_watch)
        b3.grid(row=1, column=1, pady=(30,10), sticky="")

        # pack each section then pack the frame as a whole
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
    
    def start_page(self):
        self.frame.pack()
    
    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

    def run_stop_watch(self):
        start_time = time.time()
        global running; running = True

        while running:
            elapsed_time = time.time() - start_time
            minute, second = (elapsed_time // 60, elapsed_time % 60)
            second = round(second, 2)
            minute =  int(minute)

            self.displayed_time.set(f"{minute}:{second}")

            # update the time
            self.master.update()
            time.sleep(.01)

    def stop_stop_watch(self):
        global running; running = False

    def reset_stop_watch(self):
        self.displayed_time.set('00:00.00')

######################## MAIN ###########################
if __name__ == '__main__':
    root = tk.Tk()
    # root.configure(bg="#749CBB")
    # root.geometry("750x500")
    
    # generate the GUI
    app = Workout1(root)
    # display the GUI 
    root.mainloop()