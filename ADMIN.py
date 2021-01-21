from tkinter import *
from tkinter import messagebox
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


#DELETE Function
def delete():
    num = int(ID_no.get())
    sql_Delete_query = "DELETE FROM Users WHERE id=%s"

    mycursor.execute(sql_Delete_query, [num])

    messagebox.showinfo("ADMIN"," delete succesfully")

    mydb.commit()


def get(id):
    try:
        val = int(id)  # check input is integer or not
        try:
            mycursor.execute("SELECT * FROM Users")
            student = mycursor.fetchall()
             diplay_names(student)

        except:
             diplay_names("Database error")
    except:
        display_names("Check input")






diplay_names = Listbox(od, bg="pink", fg="black", width=60, selectbackground="orange", selectforeground="black")
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
insert_button.place(x=100,y=450)

get_button = Button(od,text="GET",bg="Magenta")
get_button.place(x=200,y=450)

delete_button = Button(od,text="DELETE",bg="Magenta",command=delete)
delete_button.place(x=300,y=450)

update_button = Button(od,text="UPDATE",bg="Magenta")
update_button.place(x=400,y=450)




od.mainloop()