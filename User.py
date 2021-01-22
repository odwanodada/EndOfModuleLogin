from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

window = Tk ()
window.title("User Page")
window.geometry("500x500")



mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoicesonline', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()


def Login():
    user_verify = ID_attendance.get()
    sql = "UPDATE  Users SET Sign_in=CURRENT_TIMESTAMP() where id=%s"

    mycursor.execute(sql,[user_verify])
    results = mycursor.fetchall()
    if results:
        for x in results:
            logged()
            break

    else:
            failed()

def logged():
    messagebox.showinfo("Login Page","You have successfully logged")
    ID_attendance.delete(0, END)



def failed():
    messagebox.showinfo("Login","You failed")
    ID_attendance.delete(0, END)







heading = Label(window, text='USER PAGE ',font='times 30 bold underline',fg='black',bg='#D9D5D9')
heading.place(x=150,y=20)

ID = Label(window,text="Enter ID")
ID.place(x=70,y=100)

ID_attendance = Entry(window)
ID_attendance.place(x=180,y=100)

Signin_button = Button(window,text="Signin",bg="Magenta",command=Login)
Signin_button.place(x=100,y=220)

Signout_button = Button(window,text="Signout",bg="Magenta",)
Signout_button.place(x=200,y=220)

reg_button = Button(window,text="Registration",bg="Magenta",)
reg_button.place(x=300,y=220)

window.mainloop()