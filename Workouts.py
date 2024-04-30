import tkinter as tk
from Page import Page

# The Workout 1 class. Root class that initializes all other pages.
# Also displays the first page.
class Workout1(Page):
    def __init__(self, root=None):
        
        # creates root page (page 1).
        self.root = root
        self.frame = tk.Frame(self.root, bg = "#749CBB")
        self.frame.pack()
        
        # initializes the page GUI.
        Page.__init__(self, self.frame, self.root, "One")
        
        # initializes workout pages 1 and 2.
        self.page_2 = Workout2(master=self.root, app=self)
        self.page_3 = Workout3(master=self.root, app=self)
    
    # Starts page 1.
    def main_page(self):
        self.frame.pack()
    
    # Starts page 2.
    def make_next_page(self):
        self.frame.pack_forget()
        self.page_2.start_page()

# The Workout 2 class. Displays second page.
class Workout2(Page):
    def __init__(self, master=None, app=None):
        
        # Creates page 2.
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, bg = "#749CBB")
        
        # Initializes the page GUI.
        Page.__init__(self, self.frame, self.master, "Two")
    
    # Starts page 2.
    def start_page(self):
        self.frame.pack()
    
    # Starts page 3.
    def make_next_page(self):
        self.frame.pack_forget()
        self.app.page_3.start_page()

# The Workout 3 class. Displays third page
class Workout3(Page):
    def __init__(self, master=None, app=None):
        
        # Creates page 3.
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, bg = "#749CBB")
        Page.__init__(self, self.frame, self.master, "Three")
    
    # starts page 3.
    def start_page(self):
        self.frame.pack()
    
    # starts page 1.
    def make_next_page(self):
        self.frame.pack_forget()
        self.app.main_page()

######################## MAIN ###########################

# Main page loop.
if __name__ == '__main__':
    root = tk.Tk()
    
    # Generates the GUI.
    app = Workout1(root)
    
    # Display the GUI.
    root.mainloop()