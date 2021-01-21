from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

window = Tk ()
window.title("LOGIN PAGE")
window.geometry("500x500")

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1', database='Hospital', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()



window.mainloop()