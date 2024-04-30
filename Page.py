import tkinter as tk
import time

# Stopwatch class. Gives functionality to the stopwatch that is seen on pages 1-3
class Stopwatch:
    
    def __init__(self, root = None):
        self.root = root
        self.elapsed_time = 0
        
    def run_stop_watch(self):
        start_time = time.time() - self.elapsed_time
        global running; running = True
        
        while running:
            self.elapsed_time = time.time() - start_time
            minute, second = (self.elapsed_time // 60, self.elapsed_time % 60)
            second = f"{second:05.2f}"
            minute = int(minute)
            minute = f"{minute:02d}"
            
            self.displayed_time.set(f"{minute}:{second}")
            
            # update the time
            self.root.update()
            time.sleep(.01)
    
    def stop_stop_watch(self):
        global running; running = False
    
    def reset_stop_watch(self):
        self.displayed_time.set('00:00.00')
        self.elapsed_time = 0

# This class contains the functions for setting up GUI for pages 1-3
class Page(Stopwatch):
    def __init__(self, frame, root, workout):
        self.frame = frame
        self.root = root
        self.workout = workout
        Stopwatch.__init__(self, self.root)
        
    # Initializes all widgets on the page
    # Sets up 3 different sections on the page using tk.Frame
    
    # Frame 1 setup
        self.frame1 = tk.Frame(self.frame, bg = "#749CBB")
        
        t1 = tk.Label(self.frame1, text = f"Workout {self.workout}", fg = "white",
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
                       font = ("texgyreadventor-regular", 20), command = self.make_next_page)
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

