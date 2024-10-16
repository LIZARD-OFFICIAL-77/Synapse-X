from tkinter import ttk,StringVar
from syncer import Syncer
from time import sleep

import multiprocessing
import scratchattach
import ttkthemes
import pathlib
import tkinter
import pickle



class ScratchLoginWindow(ttkthemes.ThemedTk):
    def __init__(self):
        super().__init__(theme="adapta",fonts=True,themebg=True)

        self.password_str = tkinter.StringVar(self)
        self.username_str = tkinter.StringVar(self)

        self.set_theme("breeze")
        self.title("Login to Scratch")
        self.geometry("400x200")
        self.resizable(0,0)
        
        self.usernamelabel = ttk.Label(self,text="Username:")
        self.usernamelabel.pack(pady=2)
        self.username = ttk.Entry(self,width=30,textvariable=self.username_str)
        self.username.pack()
        self.passwordlabel = ttk.Label(self,text="Password:")
        self.passwordlabel.pack(pady=2)
        self.password = ttk.Entry(self,width=30,show="\u2022",textvariable=self.password_str)
        self.password.pack()
        self.loginbutton = ttk.Button(self,text="Login",command=self._login)
        self.loginbutton.pack()
        self.passwordnotshown = ttk.Label(self,text="Password will be hidden for security",font=("Arial Baltic",7))
        self.passwordnotshown.pack()
    def _login(self):
        t = multiprocessing.Process(target=self.login)
        t.start()
    def login(self):
        try:
            self.wrongpassword.destroy()
        except:pass
        try:
            session = scratchattach.login(self.username_str.get(),self.password_str.get())
            with open("auth","wb") as file:
                pickle.dump(session,file)
        except Exception as e:
            print(e)
            self.wrongpassword = tkinter.Label(self,text="Either username or password is wrong",fg="red",font=("Arial Baltic",10))
            self.wrongpassword.pack()


if not pathlib.Path("auth").is_file():
    loginwindow = ScratchLoginWindow()
    while not pathlib.Path("auth").is_file():
        loginwindow.update()
    sleep(1)
    loginwindow.destroy()

with open("auth","rb") as file:
    session = pickle.load(file)


class SynapseXWindow(ttkthemes.ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux",fonts=True,themebg=True)
        
        self.geometry("400x180")
        self.resizable(0,0)
        self.title("Synapse X")

        self.mainframe = ttk.Frame(self)

        self.scr_id_str = StringVar(self)

        self.name = ttk.Label(self,text="Synapse X Cloud Hack Tool",justify="left",font=("Roboto Condensed",20),borderwidth=4,relief="sunken")
        self.name.pack(fill="none",pady=10, padx=10,anchor="w")
        
        self.scr_id_label = ttk.Label(self.mainframe,text="Enter scratch project id:")
        self.scr_id_label.grid(padx=8,row=0,column=0,sticky="we")

        self.scr_id = ttk.Entry(self.mainframe,textvariable=self.scr_id_str)
        self.scr_id.grid(row=0,column=1,sticky="we",)

        self.start_sync = ttk.Button(self.mainframe,text="Start Syncing",command=self.sync)
        self.start_sync.grid(padx=8,row=2,column=0,sticky="we")

        self.start_sync = ttk.Button(self.mainframe,text="Quit",command=exit)
        self.start_sync.grid(padx=8,row=3,column=0,sticky="we")

        self.mainframe.pack(fill="x",side="top")
    def sync(self):
        self.syncer = Syncer(
            session,
            int(self.scr_id_str.get()),
        )
        self.syncprocess = multiprocessing.Process(target=self.syncer.start)
        self.syncprocess.start()
        

SynapseXWindow().mainloop()