from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector


od = Tk ()
od.title("ADMIN PAGE")
od.geometry("500x500")

mydb = mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', host='127.0.0.1',database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

#INSERT FUNCTION
def insert():
    id = ID_no.get()
    name = Username.get()
    type = Description.get()
    cell = Cell_no.get()

    sql = "insert into Users(id, Username, Description, Cell_no) values(%s, %s, %s, %s)"
    val = (id, name, type, cell)

    try:
        mycursor.execute(sql, val)

        mydb.commit()

    except:
        messagebox.showinfo("ADMIN","Successfully")
        Username.delete(0, END)
        Description.delete(0, END)
        Cell_no.delete(0, END)
        ID_no.delete(0, END)


#DELETE Function
def delete():
    num = int(ID_no.get())
    sql_Delete_query = "DELETE FROM Users WHERE id=%s"

    mycursor.execute(sql_Delete_query, [num])

    messagebox.showinfo("ADMIN"," delete succesfully")
    ID_no.delete(0, END)

    mydb.commit()

def update():
    id = ID_no.get()
    name = Username.get()
    type = Description.get()
    cell = Cell_no.get()

    sql = "Update Users SET Username=%s,Description =%s,Cell_no=%s where id =%s;"


    mycursor.execute(sql, [(name),(type),(cell),(id)])

    mydb.commit()


def get_all():
    mycursor.execute("Select * from Users")
    for i in mycursor:
        diplay_names.insert(END, i)

def exit_window():
    message_box = messagebox.askquestion('Exit ADMIN', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        od.destroy()
        import Adimaccess
    else:
        pass

def clear_all():
    Username.delete(0, END)
    ID_no.delete(0, END)
    Description.delete(0, END)
    Cell_no.delete(0, END)
    diplay_names.delete(0, END)




diplay_names = Listbox(od, bg="pink", fg="black", width=60, selectbackground="white", selectforeground="black")
diplay_names.pack(pady=20)

id_lbl = Label(od,text="Enter I.D")
id_lbl.place(x=20,y=250)

ID_no = Entry(od)
ID_no.place(x=170,y=250)


user_lbl = Label(od,text="Enter Username")
user_lbl.place(x=20,y=300)

Username = Entry(od)
Username.place(x=170,y=300)

Description_lbl = Label(od,text="Enter Description")
Description_lbl.place(x=20,y=350)

Description = Entry(od)
Description.place(x=170,y=350)

Cell_lbl = Label(od,text="Enter Cell_no")
Cell_lbl.place(x=20,y=400)

Cell_no = Entry(od)
Cell_no.place(x=170,y=400)

insert_button = Button(od,text="INSERT",bg="Magenta",command=insert)
insert_button.place(x=80,y=450)

get_button = Button(od,text="GET",bg="Magenta",command=get_all)
get_button.place(x=170,y=450)

delete_button = Button(od,text="DELETE",bg="Magenta",command=delete)
delete_button.place(x=240,y=450)

update_button = Button(od,text="UPDATE",bg="Magenta",command=update)
update_button.place(x=330,y=450)

clear_button = Button(od,text="Clear",bg="Magenta",command=clear_all)
clear_button.place(x=10,y=450)

exit_button = Button(od,text="Exit",bg="Magenta",command=exit_window)
exit_button.place(x=430,y=450)


od.mainloop()