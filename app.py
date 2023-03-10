import requests
from bs4 import BeautifulSoup

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class App():
    def __init__(self,master):
        super().__init__()

        self.user_frame = ttk.LabelFrame(master)
        self.user_frame.grid(row=0,column=0,padx=20,pady=20,ipadx=10,ipady=10)

        self.username_label = ttk.Label(self.user_frame,text='Username:')
        self.username_label.grid(row=0,column=0,padx=30,pady=10)
        self.username_entry = ttk.Entry(self.user_frame)
        self.username_entry.grid(row=0,column=1,padx=30,pady=10,columnspan=1,sticky='EW')

        self.check_button = ttk.Button(self.user_frame,text='Check Details',command=lambda:self.search_user_details(self.username_entry.get()))
        self.check_button.grid(row=4,column=0,columnspan=3,padx=30,pady=10)

    def search_user_details(self,username):
        username = username.lower()
        user_homepage_url = f'https://www.deviantart.com/{username}'
        response = requests.get(user_homepage_url)
        response.raise_for_status
        try:
            if(response.status_code==200):
                user_homepage_source_code = response.text
        
                soup = BeautifulSoup(markup=user_homepage_source_code,features='lxml')
                number_of_watchers = soup.select(selector='.bdzzI span')[0]
                print(number_of_watchers.text)
                number_of_page_views = soup.select(selector='.bdzzI ._1QXgq')[0]
                print(number_of_page_views.text)
                number_of_deviations = soup.select(selector='.bdzzI span')[1]
                print(number_of_deviations.text)

                self.show_user_details(number_of_watchers.text,number_of_page_views.text,number_of_deviations.text)

                messagebox.showerror('App Error','Sorry but your response could not be resolved. Please try again later')
        except:
            messagebox.showerror('App Error','Request could not be made at the moment. Please check if you have internet access')

    def show_user_details(self,no_watchers,no_page_views,no_deviations):
        self.user_details_label = ttk.Label(self.user_frame,text=f'User Name: {no_watchers}\nPage Views: {no_page_views}\n Deviations: {no_deviations}')
        self.user_details_label.grid(row=2,column=0,columnspan=2)

if __name__=='__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
