from tkinter import *
from tkinter import messagebox
import mysql.connector



root = Tk ()
root.title("LOGIN PAGE")
root.geometry("500x500")


mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1', database='Lifechoicesonline', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

def Login():
    user_verify = Username.get()
    pass_verify = Password.get()
    sql = "select * from Login where Full_Name = %s and Password = %s"

    mycursor.execute(sql,[(user_verify), (pass_verify)])
    results = mycursor.fetchall()
    if results:
        for x in results:
            logged()
            break

    else:
            failed()

def logged():
    messagebox.showinfo("Login Page","You have successfully logged")
    Username.delete(0, END)
    Password.delete(0, END)
    root.destroy()
    import User



def failed():
    messagebox.showinfo("Login","You failed")
    Username.delete(0, END)
    Password.delete(0, END)


def exit_window():
    message_box = messagebox.askquestion('Exit UserApplication', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        root.destroy()
    else:
        pass


heading = Label(root, text='LOGIN PAGE ',font='times 30 bold underline',fg='black',bg='#D9D5D9')
heading.place(x=150,y=20)


user_lbl = Label(root,text="Enter Username")
user_lbl.place(x=50,y=100)

Username = Entry(root)
Username.place(x=200,y=100)

passwd_lbl = Label(root,text="Enter Password")
passwd_lbl.place(x=50,y=160)

Password = Entry(root,show= "*")
Password.place(x=200,y=160)

login_button = Button(root,text="Login",bg="Magenta",command=Login)
login_button.place(x=200,y=220)

exit_button = Button(root,text="Exit",bg="Magenta",command=exit_window)
exit_button.place(x=300,y=220)


root.mainloop()