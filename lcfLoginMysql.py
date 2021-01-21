from tkinter import *
from tkinter import messagebox



root = Tk ()
root.title("LOGIN PAGE")
root.geometry("500x500")



def Login():
    all_login={"Odwa":"Odwa123"}
    my_user= Username.get()
    password= Password.get()
    if (my_user, password)in all_login.items():
        messagebox.showinfo("INFO", "Correct Login")
        root.withdraw()
        import User

    else:
        messagebox.showinfo("INFO", "Incorrect Login")
        Username.delete(0, END)
        Password.delete(0, END)




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



root.mainloop()