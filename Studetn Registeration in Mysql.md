from tkinter import *
import MySQLdb as sql
import messagebox 
def ok():
    con = sql.connect(host = "localhost",user = "root", password = "724800",db = "class")
    cur = con.cursor()
    name = student_name_entry.get()
    age = student_age_entry.get()
    rollno = student_rollno_entry.get()
    mobileno = student_mblno_entry.get()
    gender = student_sex_entry.get()
    department = student_dept_entry.get()

    cur.execute("insert into students(name,age,rollno,mobileno,gender,department) values('"+name+"','"+age+"','"+rollno+"','"+mobileno+"','"+gender+"','"+department+"')")
    con.commit()
    con.close()
    result = cur.fetchall()
    print(result)
    messagebox.showinfo("Mysql Success","Succcessfully saved")

window =Tk()
window.geometry('700x600')
window.title("student information stored in mysql")
window.config(background="pink")

heading = Label(window,text="Student Information",font=("Arial",25,"bold"),fg="white",background="blue")
heading.pack(fill=X,pady=7)

lableframe = LabelFrame(window,text="Students Data",font=("Arial",20,"bold"),fg="white",background="grey")
lableframe.pack(fill=X)

student_name = Label(lableframe,text="Student Name",font=("Arial",15,"bold"),background="grey")
student_name.grid(row=0,column=0,pady=10)

student_name_entry = Entry(lableframe,width=20,font=("arial",15,"bold"))
student_name_entry.grid(row=0,column=1,pady=10)

student_age = Label(lableframe,text="  Student Age  ",font=("Arial",15,"bold"),background="grey")
student_age.grid(row=1,column=0,padx=10)

student_age_entry = Entry(lableframe,width=20,font=("arial",15,"bold"))
student_age_entry.grid(row=1,column=1,pady=10)

student_rollno = Label(lableframe,text="  Student Rollno  ",font=("Arial",15,"bold"),background="grey")
student_rollno.grid(row=2,column=0,pady=10,padx=10)

student_rollno_entry = Entry(lableframe,width=20,font=("arial",15,"bold"))
student_rollno_entry.grid(row=2,column=1,pady=10)

student_mblno = Label(lableframe,text="  Student Mobileno  ",font=("Arial",15,"bold"),background="grey")
student_mblno.grid(row=3,column=0,pady=10,padx=10)

student_mblno_entry = Entry(lableframe,width=20,font=("arial",15,"bold"))
student_mblno_entry.grid(row=3,column=1,pady=10)

student_sex = Label(lableframe,text="  Student Gender  ",font=("Arial",15,"bold"),background="grey")
student_sex.grid(row=4,column=0,pady=10,padx=10)

student_sex_entry = Entry(lableframe,width=20,font=("arial",15,"bold"))
student_sex_entry.grid(row=4,column=1,pady=10)

student_dept = Label(lableframe,text="  Student Department  ",font=("Arial",15,"bold"),background="grey")
student_dept.grid(row=5,column=0,pady=10,padx=10)

student_dept_entry = Entry(lableframe,width=20,font=("arial",15,"bold"))
student_dept_entry.grid(row=5,column=1,pady=10)

button = Button(lableframe,text="Submit",relief=RIDGE,font=("Arial",15,"bold"),activebackground="red",background="green",command=ok)
button.grid(row=6,column=1,pady=15)

window.mainloop()
