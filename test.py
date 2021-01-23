from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

root1 = Tk ()
root1.title("REGISTRATION PAGE")
root1.geometry("500x500")

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1', database='Lifechoicesonline', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

def reg_function():
    id = ID_no.get()
    name = Username.get()
    type = Description.get()
    cell = Cell_no.get()

    sql = "insert into Users(id, Username, Description, Cell_no) values(%s, %s, %s, %s)"
    val = (id, name, type, cell)


    mycursor.execute(sql, val)

    mydb.commit()

    messagebox.showinfo("REGISTRATION PAGE", "Successfully REGISTRATION")

    root1.destroy()
    import User




heading = Label(root1, text='REGISTRATION PAGE ',font='times 30 bold underline',fg='black',bg='#D9D5D9')
heading.pack()




id_lbl = Label(root1,text="Enter I.D")
id_lbl.place(x=20,y=100)

ID_no = Entry(root1)
ID_no.place(x=170,y=100)

user_lbl = Label(root1,text="Enter Username")
user_lbl.place(x=20,y=150)

Username = Entry(root1)
Username.place(x=170,y=150)

Description_lbl = Label(root1,text="Enter Description")
Description_lbl.place(x=20,y=200)

Description = Entry(root1)
Description.place(x=170,y=200)

Cell_lbl = Label(root1,text="Enter Cell_no")
Cell_lbl.place(x=20,y=250)

Cell_no = Entry(root1)
Cell_no.place(x=170,y=250)

reg_button = Button(root1,text="Registration",bg="Magenta",command=reg_function)
reg_button.place(x=200,y=300)



root1.mainloop()