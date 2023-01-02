import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self,master):
        super().__init__()


        self.username_label = ttk.Label(master,text='Username:')
        self.username_label.grid(row=0,column=0,padx=30,pady=10)
        self.username_entry = ttk.Entry(master)
        self.username_entry.grid(row=0,column=1,padx=30,pady=10,columnspan=1,sticky='EW')

        self.check_button = ttk.Button(master,text='Check')
        self.check_button.grid(row=4,column=1,columnspan=2,padx=30,pady=10)

if __name__=='__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
