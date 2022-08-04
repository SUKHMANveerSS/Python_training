from tkinter import*
from mysql import connector

def database():
    conn = connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        port='3306',
        database='python')
    mycursor = conn.cursor()
    mycursor.execute("insert into regisform values(%s,%s,%s,%s,%s,%s)",
                     (var.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
    conn.commit()

top = Tk()
top.geometry("400x250")

rform = Label(top, text="REGISTERATION FORM", font=("bold")).place(x=30, y=10)
Srno = Label(top, text="Sr.no.").place(x=30, y=50)
Name = Label(top, text="Name").place(x=30, y=90)
Rollno = Label(top, text="Roll.no.").place(x=30, y=130)
Address = Label(top, text="Address").place(x=30, y=170)
Branch = Label(top, text="Branch").place(x=30, y=210)
Gender = Label(top, text="Gender:").place(x=30, y=250)
var = IntVar()
Radiobutton(top, text="Male", variable=var, value=1).place(x=80, y=250)
Radiobutton(top, text="Female", variable=var, value=2).place(x=130, y=250)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue",command=database).place(x=30, y=300)
e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=95, y=130)
e4 = Entry(top).place(x=95, y=170)
e5 = Entry(top).place(x=95, y=210)

top.mainloop()