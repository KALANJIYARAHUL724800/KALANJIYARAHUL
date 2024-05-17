# My Login Form Creation
from tkinter import *
from tkinter import  messagebox
def ok(): #Button Condition Action
    if nameEntry.get().lower() == 'admin' and pwdEntry.get().lower() == 'admin': #  If condition to equal and any type of here the label we consider only lower case ADMIN,AdmIN = admin
        messagebox.showinfo("Successfully","Succesfully Submited")
root = Tk()
root.geometry("500x300")
headinglabel = Label(root,text="Login Form Kl Rahul Software",fg="black",font=("times of new roman",25,"bold"),bg="light grey")
headinglabel.pack(fill=X)
frame = Frame(root,bg="light pink",height=500,width=500)
frame.pack(fill=X,pady=10)

namelabel = Label(frame,text="User Name  ",font=("times of new roman",15,"bold"),bg="light pink")
namelabel.grid(row=0,column=0,padx=10,pady=20)

nameEntry = Entry(frame,font=("times of new roman",15,"bold"),relief=RIDGE)
nameEntry.grid(row=0,column=1)

pwdlabel = Label(frame,text="Password", font=("times of new roman",15,"bold"),bg="light pink")
pwdlabel.grid(row=1,column=0,padx=5,pady=5)

pwdEntry = Entry(frame,font=("times of new roman",15,"bold"),relief=RIDGE)
pwdEntry.grid(row=1,column=1)

btn = Button(frame,text="Submit",font=("times of new roman",15,"bold"),relief=RIDGE,height=1,width=12,command=ok) #button creation and command set
btn.grid(row=3,column=1,pady=50)

root.mainloop()
