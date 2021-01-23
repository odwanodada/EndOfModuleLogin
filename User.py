from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector


window = Tk ()
window.title("User Page")
window.geometry("500x500")




mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1',database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

def reg():
    window.destroy()
    import test

def Login():
    user_verify = ID_entry.get()
    sql = "UPDATE Users SET Sign_in=CURRENT_TIMESTAMP() WHERE id=%s"

    mycursor.execute(sql, (user_verify,))
    messagebox.showinfo("USER PAGE","DATE&TIME Successfully UPDATED")
    ID_entry.delete(0, END)


    mydb.commit()

def LogOut():
    user_verify = ID_entry.get()
    sql = "UPDATE Users SET Sign_out=CURRENT_TIMESTAMP() WHERE id=%s"

    mycursor.execute(sql, (user_verify,))
    messagebox.showinfo("USER PAGE","DATE&TIME Successfully UPDATED")
    ID_entry.delete(0, END)


    mydb.commit()

def exit_window():
    message_box = messagebox.askquestion('Exit ADMIN', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        window.destroy()
        import lcfLoginMysql
    else:
        pass


heading = Label(window, text='USER PAGE ',font='times 30 bold underline',fg='black',bg='#D9D5D9')
heading.place(x=150,y=20)

ID = Label(window,text="Enter ID")
ID.place(x=70,y=100)

ID_entry= Entry(window)
ID_entry.place(x=180,y=100)

Signin_button = Button(window,text="Signin",bg="Magenta",command=Login)
Signin_button.place(x=100,y=220)

Signout_button = Button(window,text="Signout",bg="Magenta",command=LogOut)
Signout_button.place(x=200,y=220)

reg_button = Button(window,text="Registration",bg="Magenta",command=reg)
reg_button.place(x=300,y=220)

exit_button = Button(window,text="Exit",bg="Magenta",command=exit_window)
exit_button.place(x=420,y=220)

window.mainloop()