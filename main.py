from tkinter import *
from tkinter import ttk
import tkinter
import get_movie
from tkinter import messagebox

import get_movie as MOV


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(padding=(6, 4))
        self.pack()
        self.make_style()
        self.create_widget()

    def make_style(self):
        pass

    def create_widget(self):
        #所得動画のURL
        Label_url = ttk.Label(self, text='動画のURL', padding=(5, 2))
        Label_url.grid(row=0, column=0, sticky=E)

        self.urlstr = StringVar()
        url_entry = ttk.Entry(self, width=20)
        url_entry.configure(textvariable=self.urlstr)
        url_entry.grid(row=0, column=1)
  

        #所得動画の保存先
        Label_save = ttk.Label(self, text='動画の保存先', padding=(5, 5))
        Label_save.grid(row=1, column=0, sticky=E)

        self.savepathstr = StringVar()
        save_entry = ttk.Entry(self,  width=20)
        save_entry.configure(textvariable=self.savepathstr)
        save_entry.grid(row=1, column=1)

        #所得動画の保存名
        Label_name = ttk.Label(self, text='保存名', padding=(5, 5))
        Label_name.grid(row=2, column=0, sticky=E)

        self.namestr = StringVar()
        name_entry = ttk.Entry(self, width=20)
        name_entry.configure(textvariable=self.namestr)
        name_entry.grid(row=2, column=1)

        #保存ボタン  
        button_OK = ttk.Button(self, text='保存', command=self.check_text, padding=(5, 5))
        button_OK.grid(row=3, column=0, sticky=E)

        
    def hello(self):
        print('Hello')

    def check_text(self):     
        if len(self.urlstr.get())==0 or len(self.savepathstr.get()) == 0 or len(self.namestr.get()) == 0:
            messagebox.showinfo('確認してください', '動画URL、保存先、保存名をすべて入力してください')
        else:
            MOV.Do_Download(self.urlstr.get(), self.savepathstr.get(), self.namestr.get())
            self.urlstr = ""
            self.savepathstr = ""
            self.namestr = ""


root = Tk()
root.title('install movie')
root.minsize(width=250, height=150)
#frame = ttk.Frame(root, padding=10)
frame = MainFrame(root)
frame.grid()
root.mainloop()