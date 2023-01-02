import requests
from bs4 import BeautifulSoup

import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self,master):
        super().__init__()

        self.username_label = ttk.Label(master,text='Username:')
        self.username_label.grid(row=0,column=0,padx=30,pady=10)
        self.username_entry = ttk.Entry(master)
        self.username_entry.grid(row=0,column=1,padx=30,pady=10,columnspan=1,sticky='EW')

        self.check_button = ttk.Button(master,text='Check',command=lambda:self.search_user_details(self.username_entry.get()))
        self.check_button.grid(row=4,column=0,columnspan=3,padx=30,pady=10)

    def search_user_details(self,username):
        user_homepage_url = f'https://www.deviantart.com/{username}'
        user_homepage_source_code = requests.get(user_homepage_url).text
        print(user_homepage_source_code)

if __name__=='__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
