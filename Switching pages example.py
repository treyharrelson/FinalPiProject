import tkinter as tk

class App:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame, text='Main page').pack()
        tk.Button(self.frame, text='Go to Page 2',
                  command=self.make_page_2).pack()
        self.page_2 = Page_2(master=self.root, app=self)
        self.page_3 = Page_3(master=self.root, app=self)

    def main_page(self):
        self.frame.pack()

    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()


class Page_2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Page 2').pack()
        tk.Button(self.frame, text='Page 3', command=self.make_page_3).pack()

    def start_page(self):
        self.frame.pack()

    def make_page_3(self):
        self.frame.pack_forget()
        self.app.page_3.start_page()

class Page_3:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Page 3').pack()
        tk.Button(self.frame, text='Page 3', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()