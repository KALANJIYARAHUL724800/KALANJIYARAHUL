# Modules----------
import messagebox 
from tkinter import *
import MySQLdb as sql

# Login page creation function------------------
def ok():
    if user_entry.get().lower() != 'admin' and password_entry.get().lower() != 'admin':
        messagebox.showerror("Sorry","Your user name and password is not matched!")
    if user_entry.get().lower() == 'admin' and password_entry.get().lower() == 'admin':
        user_entry.config(show='*')
        messagebox.showinfo("Successfully","Succesfully Submited")
    
# Insert,Read,update,Delete Fucntions------------------
        def insert():
            con = sql.connect(host='localhost',user='root',password='724800',db='Library') 
            cur = con.cursor()
            Insert = BookID_entry.get()
            Read = Title_entry.get()
            Author = Author_entry.get()
            Year = YearPublished_entry.get()
            Genre = Genre_entry.get()
            ISBN = ISBN_entry.get()
            cur.execute("insert into Books(BookID,Title,Author,YearPublished,Genre,ISBN) values('"+Insert+"','"+Read+"','"+Author+"','"+Year+"','"+Genre+"','"+ISBN+"')")
            con.commit()
            con.close()
            messagebox.showinfo('success','Successfully Data Added!..')
            result = cur.fetchall()
            for i in result:
                print(i)
        def read():
            messagebox.showinfo('Sucess','Show all the data')
            con = sql.connect(host='localhost',user='root',password='724800',db='Library') 
            cur = con.cursor()
            cur.execute("select * from Books limit 5")

            i = 0
            for Books in cur:
                for j in range(len(Books)):
                    head = Canvas(window)
                    e = Entry(head,width=150,fg='blue',font=('arial',10,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END,Books[j])
                    i = i + 1
                    head.pack()
            print("Insert Successfull")
            result = cur.fetchall()
            for i in result:
                print(i)
        def update():
            con = sql.connect(host='localhost',user='root',password='724800',db='Library') 
            cur = con.cursor()
            Insert = BookID_entry.get()
            Read = Title_entry.get()
            Author = Author_entry.get()
            Year = YearPublished_entry.get()
            Genre = Genre_entry.get()
            ISBN = ISBN_entry.get()
            args = (Insert,Read,Author,Year,Genre,ISBN)
            query = 'UPDATE Books SET Title=%s, Author=%s, Yearpublished=%s, Genre=%s, ISBN=%s WHERE BookID = %s'
            cur.execute(query,(Read,Author,Year,Genre,ISBN,Insert)) 
            con.commit()
            con.close()
            messagebox.showinfo('Update','Successfully Data updated!..')

            result = cur.fetchall()
            for i in cur:
                print(i)
        def delete():
            messagebox.showinfo('Truncated','Successfully Data was Deleted')
            con = sql.connect(host='localhost',user='root',password='724800',db='Library') 
            cur = con.cursor()
            cur.execute("truncate Books")
            con.commit()
            con.close()

        # Create Tkinter--------
        window = Tk()
        window.title('Mysql and Python')
        window.config(background='light pink')
        window.geometry('1000x900')

        #heading Label
        head = Label(window,text="MYSQL CONNECT WITH PYTHON",font=("arial",19,"bold"),background="yellow",relief=GROOVE)
        head.pack(fill=X,pady=5,padx=15)

        # Default Light pink color ------------
        color = 'light pink'

        # Frame set 1st-------------------
        frame = LabelFrame(window,background=color,text="Book Collection Manager",font=('arial',15,'bold'),padx=200)

        BookID = Label(frame,text="BookID              : ",font=('arial',10,'bold'),background=color)
        BookID.grid(row=1,column=1,padx=15)

        BookID_entry = Entry(frame,font=('arial',10,'bold'),width=30)
        BookID_entry.grid(row=1,column=2,pady=10,padx=10)

        Title = Label(frame,text="Title                  :",font=('arial',10,'bold'),background=color)
        Title.grid(row=2,column=1,padx=15,pady=10)

        Title_entry = Entry(frame,font=('arial',10,'bold'),width=30)
        Title_entry.grid(row=2,column=2,padx=10)

        Author = Label(frame,text="Author              :",font=('arial',10,'bold'),background=color)
        Author.grid(row=3,column=1,padx=15)

        Author_entry = Entry(frame,font=('arial',10,'bold'),width=30)
        Author_entry.grid(row=3,column=2,pady=10,padx=10)

        YearPublished = Label(frame,text="YearPublished :",font=('arial',10,'bold'),background=color)
        YearPublished.grid(row=4,column=1,padx=15)

        YearPublished_entry = Entry(frame,font=('arial',10,'bold'),width=30)
        YearPublished_entry.grid(row=4,column=2,pady=10,padx=20)

        Genre = Label(frame,text="Genre               :",font=('arial',10,'bold'),background=color)
        Genre.grid(row=5,column=1,padx=15)

        Genre_entry = Entry(frame,font=('arial',10,'bold'),width=30)
        Genre_entry.grid(row=5,column=2,pady=10,padx=10)

        ISBN = Label(frame,text="ISBN                 :",font=('arial',10,'bold'),background=color)
        ISBN.grid(row=6,column=1,padx=15)

        ISBN_entry = Entry(frame,font=('arial',10,'bold'),width=30)
        ISBN_entry.grid(row=6,column=2,pady=10,padx=10)

        frame.pack()

        # Create Buttons and Calling fuctions ------------------------
        button_frame = LabelFrame(window,text="Buttons",font=('arial',15,"bold"),background=color,height=50,width=300,padx=220)

        create_button = Button(button_frame,text="INSERT",font=("arial",12,"bold"),background="green",fg="white",relief=GROOVE,command=insert,activebackground="yellow")
        create_button.grid(row=0,column=2,padx=10,pady=20)

        Read_button = Button(button_frame,text="READ",font=("arial",12,"bold"),background="green",fg="white",relief=GROOVE,command=read,activebackground="yellow")
        Read_button.grid(row=0,column=3,padx=10,pady=20)

        Update_button = Button(button_frame,text="UPDATE",font=("arial",12,"bold"),background="green",fg="white",relief=GROOVE,command=update,activebackground="yellow")
        Update_button.grid(row=0,column=4,padx=10,pady=20)

        Delete_button = Button(button_frame,text="DELETE",font=("arial",12,"bold"),background="red",fg="white",relief=GROOVE,command=delete,activebackground='yellow')
        Delete_button.grid(row=0,column=5,padx=10,pady=20)

        button_frame.pack(pady=20)

        # Tab key pressed in bind of the function(Enter button click Tab button also Entered)-------------
        window.bind('<Return>', 'event generate %W <Tab>')
        
        # Closing the main loop of the first program
        window.mainloop()

# Simple login page tkinter creation----------
root = Tk()
root.title('Login page')
root.geometry('500x400')
root.config(background="light blue")
heading = Label(root,text="Welcome to Login Page",font=('Times of new roman',20,'bold'),padx=10,relief=GROOVE,background='black',fg='white')
heading.pack(fill=X,pady=20,padx=20)

user = LabelFrame(root,text="Login Form ",font=('Times of new roman',20,'bold'),background='light blue',pady=20)

user_name = Label(user,text="User Name : ",font=('Times of new roman',15,'bold'),background='light blue')
user_name.grid(row=0,column=1,padx=5,pady=20)

user_entry = Entry(user,font=('Times of new roman',15,'bold'))
user_entry.grid(row=0,column=2,padx=10,pady=20)

password = Label(user,text="Password  : ",font=('Times of new roman',15,'bold'),background='light blue')
password.grid(row=1,column=1,padx=5,pady=25)

# password hiding to the method (show ='*' --> if any input only show for * of the output)--------------------
password_entry = Entry(user,font=('Times of new roman',15,'bold'),show='*')
password_entry.grid(row=1,column=2,padx=10,pady=25)
user.pack(pady=15)

# login page submit button  creation ---------------
btn = Frame(root,background='light blue')
button = Button(btn,text="Submit",font=('arial',10,'bold'),background='yellow',activebackground='green',relief=GROOVE,height=2,width=15,command=ok)
button.grid(row=0,column=1)
btn.pack()

# root login page tab key press funciton ------------------
root.bind('<Return>', 'event generate %W <Tab>')
root.mainloop()