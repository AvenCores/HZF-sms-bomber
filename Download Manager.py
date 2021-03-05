from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title('HZF Bomber Downloader')
root.geometry('350x120')
root.resizable(width=False, height=False)

def download():
        f=open(r'C:\Users\%username%\Downloads\HZF Bomber.zip',"wb")
        ufr = requests.get("https://github.com/AvenCores/HZF-sms-bomber/releases/download/V1.2/HZF.SMS.BOMBER.V1.2.zip")
        f.write(ufr.content)
        f.close()
        messagebox.showinfo(title="Удачно", message='Бомбер был скачен в Download')
        return "exit"

file = Button(text='Скачать HZF Bomber V1.2', command=download)
file.pack()
file.place(x=100, y=30)
poetry = 'Downloader manager by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=90)
root.mainloop()
