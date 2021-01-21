from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

root = Tk ()
root.title("LOGIN PAGE")
root.geometry("500x500")

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1', database='Hospital', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()


heading = Label(root, text='LOGIN PAGE ',font='times 30 bold underline',fg='black',bg='#D9D5D9')
heading.pack()





root.mainloop()