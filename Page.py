import tkinter as tk
import time

# Stopwatch class. Gives functionality to the stopwatch that is seen on pages 1-3.
class Stopwatch:
    
    def __init__(self, root = None):
        self.root = root
        self.elapsed_time = 0
        
        # Starts timer.
    def run_stop_watch(self):
        start_time = time.time() - self.elapsed_time
        global running; running = True
        
        # Calculates time.
        while running:
            self.elapsed_time = time.time() - start_time
            minute, second = (self.elapsed_time // 60, self.elapsed_time % 60)
            second = f"{second:05.2f}"
            minute = int(minute)
            minute = f"{minute:02d}"
            
            self.displayed_time.set(f"{minute}:{second}")
            
            # Update the time.
            self.root.update()
            time.sleep(.01)
    
    # Pauses the Stop Watch
    def stop_stop_watch(self):
        global running; running = False
    
    def reset_stop_watch(self):
        self.displayed_time.set('00:00.00')
        self.elapsed_time = 0



# This class contains the functions for setting up GUI for pages 1-3.
class Page(Stopwatch):

    data = [0, 1, 2]
    
    def __init__(self, frame, root, pageint, workout=None):
        self.frame = frame
        self.root = root
        self.pageint = pageint
        self.workout = workout
        self.ready_to_switch = False
        Stopwatch.__init__(self, self.root)
        
        
    # Initializes all widgets on the page.
    # Sets up 3 different sections on the page using tk.Frame.
    # Frame 1 setup.
        self.frame1 = tk.Frame(self.frame, bg = "#749CBB")
        
        t1 = tk.Label(self.frame1, text = f"Workout {self.workout}", fg = "white",
                      bg = "#749CBB", font = ("texgyreadventor-regular",30))
        t1.grid(row=0, column=0, pady=(10,0), sticky="")
        
        
    # Frame 2 setup.
        self.frame2 = tk.Frame(self.frame, bg = "#749CBB")
        
        t3 = tk.Label(self.frame2, text = 'Weight Lifted (lbs):', font = ("texgyreadventor-regular", 10))
        t3.grid(row=0, column=0, padx=(10,0), sticky="")
        
        self.entry = tk.Entry(self.frame2, bd = 5, width= 4, bg = 'white', font = ("texgyreadventor-regular"), 
                         fg = 'black')
        self.entry.grid(row=0, column=1, padx=(5, 5), sticky="")
        
        # Get the values from the entry and send to an array.
        enter = tk.Button(self.frame2, text = 'Enter', fg = "white", bg = "#748CBB",
                       font = ("texgyreadventor-regular", 15), command = self.get_value)
        enter.grid(row=0, column=2, padx=(0,340), sticky="")
        
        b4 = tk.Button(self.frame2, text = 'Next Workout', fg = "white", bg = "#9E6CA8",
                       font = ("texgyreadventor-regular", 20), command = self.make_next_page)
        b4.grid(row=0, column=3, padx=(0,10), sticky="")
        
        self.invalidEntry = tk.StringVar()
        self.invalidEntry.set(" \n")
        Invalid_Entry = tk.Label(self.frame2, textvariable = self.invalidEntry, bg = "#749CBB", font = ("texgyreadventor-regular", 10))
        Invalid_Entry.grid(row=1, column=0, columnspan=2, sticky="")
        
        self.displayed_time = tk.StringVar()
        timer = tk.Label(self.frame2, textvariable = self.displayed_time, fg = "black", bg = "white",
                         font = ("texgyreadventor-regular", 40))
        self.displayed_time.set('00:00.00')
        timer.grid(row=2, column=0, columnspan=4, pady=(30,20), sticky="")
        
        
    # Frame 3 setup.
        self.frame3 = tk.Frame(self.frame, bg = "#749CBB")
        
        b1 = tk.Button(self.frame3, text = 'Play', fg = "white", bg = "#5B8C5D",
                       font = ("texgyreadventor-regular", 50), command = self.run_stop_watch)
        b1.grid(row=0, column=0, padx=30, sticky="")
        
        b2 = tk.Button(self.frame3, text = 'Stop', fg = "white", bg = "#9C4B60",
                       font = ("texgyreadventor-regular", 50), command = self.stop_stop_watch)
        b2.grid(row=0, column=1, padx=30, sticky="")
        
        
    # Frame 4 setup
        self.frame4 = tk.Frame(self.frame, bg = "#749CBB")
        
        b3 = tk.Button(self.frame4, text = 'Start Workout Over', fg = "white", bg = "#748CAA",
                       font = ("texgyreadventor-regular", 20), command = self.start_over)
        b3.grid(row=1, column=0, pady=(30,10), sticky="")
        
        b4 = tk.Button(self.frame4, text = 'Reset timer', fg = "white", bg = "#748CBB",
                       font = ("texgyreadventor-regular", 20), command = self.reset_stop_watch)
        b4.grid(row=1, column=1, padx=(100,0), pady=(30,10), sticky="")
        
        
        # Pack each section to the main-frame.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
    
    # Retrieves use input value.
    def get_value(self):
        e_text=self.entry.get()
        
        # Tests to see if input is a valid integer greater than 0 and less than 1400.
        try:
            isinstance(int(e_text), int)
        except:
            self.invalidEntry.set("Invalid Entry. Please input \nthe weight being lifted.")
            Invalid_Entry = tk.Label(self.frame2, textvariable = self.invalidEntry, bg = "white", font = ("texgyreadventor-regular", 10))
            Invalid_Entry.grid(row=1, column=0, columnspan=2, sticky="")
            self.ready_to_switch = False
        else:
            if 0 < int(e_text) <= 1400:
                self.ready_to_switch = True
                Page.data[self.pageint - 1] = int(e_text)
                self.invalidEntry.set(" \n")
                Invalid_Entry = tk.Label(self.frame2, textvariable = self.invalidEntry, bg = "#749CBB", font = ("texgyreadventor-regular", 10))
                Invalid_Entry.grid(row=1, column=0, columnspan=2, sticky="")
                
        print (Page.data)


# This class contains the functions for setting up GUI for page 4.
class ResultsPage:
    def __init__(self, frame, root):
        self.frame = frame
        self.root = root
        
        
    # Frame 1 setup.
        self.frame1 = tk.Frame(self.frame, bg = "#749CBB")
        
        t1 = tk.Label(self.frame1, text = f"Workout Results", fg = "white",
                      bg = "#749CBB", font = ("texgyreadventor-regular",30))
        t1.grid(row=0, column=0, pady=(10,0), sticky="")
        
        
    # Frame 2 setup.
        self.frame2 = tk.Frame(self.frame, bg = "#749CBB")
        
        self.Make_Table()
        
        
    # Frame 3 setup.
        self.frame3 = tk.Frame(self.frame, bg = "#749CBB")
        
        b1 = tk.Button(self.frame3, text = 'Start Workout Over', fg = "white", bg = "#748CAA",
                       font = ("texgyreadventor-regular", 20), command = self.start_over)
        b1.grid(row=1, column=0, pady=(30,10), sticky="")
        
    # Pack each section to the main-frame.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
    
    # creates
    def Make_Table(self):
        
        # PUT SENSOR VARIABLES IN PLACE OF 1, 2, 3, 4
        
        # take the data
        list = [
            ("One Rep Max", 1),
            ("Rep Change", 2),
            ("Weight Change", 3),
            ("Reps", 4)
            ]

        # find total number of rows and
        # columns in list
        total_rows = len(list)
        total_columns = len(list[0])
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                
                table_text = tk.StringVar()
                table_text.set(list[i][j])
                table = tk.Label(self.frame2, textvariable = table_text, 
                                      highlightbackground="blue", highlightthickness=2, 
                                      width=20, fg='blue', font=('Arial',16,'bold'))
                table.grid(row=i, column=j)

