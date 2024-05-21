from tkinter import *
import MySQLdb as sql
def ok():
    con = sql.connect(host="localhost",user="root",password="724800",db="class")
    cur = con.cursor()
    name = n1_e.get()
    age = n2_e.get()

    cur.execute("insert into student(name,age) values('"+name+"','"+age+"')")
    con.commit()
    con.close()
    print("Insert Successfull")
    result = cur.fetchall()
    print(result)
    
window = Tk()
window.geometry("300x300")
window.title("Simple Data Entry to Connect Mysql database project")
n1 = Label(window,text="Name",font=("arial",10,"bold"))
n1.grid(row=0,column=0,pady=10)

n2 = Label(window,text="Age",font=("arial",10,"bold"))
n2.grid(row=1,column=0,padx=10)

n1_e = Entry(window)
n1_e.grid(row=0,column=1,padx=10)

n2_e = Entry(window)
n2_e.grid(row=1,column=1,padx=10)

button = Button(window,text="Submit",background="yellow",font=("Arial",10,"bold"),command=ok,activebackground="blue")
button.grid(row=4,column=1,pady=10)
window.mainloop()
