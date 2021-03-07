from tkinter import *
from tkinter import messagebox
import os
import requests

root = Tk()
root.title('Download Manager')
root.geometry('350x140')
root.resizable(width=False, height=False)

def downloadSms():
        path = 'c:/Bomber'
        try:
            os.mkdir(path)
        except OSError as error:
            print(error) 
        f=open(r'c:/Bomber/HZF Bomber.zip',"wb")
        ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.2/HZF.SMS.BOMBER.V1.2.zip")
        f.write(ufr.content)
        f.close()
        messagebox.showinfo(title="Удачно", message='SMS Bomber был скачен в папку C:\Bomber')
        return "exit"

def downloadEmail():
        path = 'c:/Bomber'
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        f=open(r'c:/Bomber/HZF Email Bomber.zip', "wb")
        ufr = requests.get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.0/Email.Bomber.by.HZF.zip")
        f.write(ufr.content)
        f.close()
        messagebox.showinfo(title="Удачно", message='Email Bomber был скачен в папку C:\Bomber')
        return "exit"


file = Button(text='Скачать HZF Bomber V1.2', command=downloadSms)
file.pack()
file.place(x=11, y=26)
file = Button(text='Скачать HZF Email Bomber V1.2', command=downloadEmail)
file.pack()
file.place(x=11, y=63)
poetry = 'Downloader manager by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=110)
root.mainloop()
