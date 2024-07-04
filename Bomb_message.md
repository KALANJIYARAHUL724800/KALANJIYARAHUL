# Modules
from tkinter import *
import pyautogui
import time as t
import messagebox
# functions 
def ok():
    global a,b
    a = label1.get()
    b = msg1.get()
    # conditons with logic
    if a=='0' and b =='0':
        messagebox.showerror('Error','Please fill the Entry Required!!!!')
    if a!="0" or b!='0':
        t.sleep(5)
        for i in range(int(a)):
            pyautogui.typewrite(str(b))
            pyautogui.press('enter')
# Tkinter frame work base
window = Tk()
window.geometry('310x400')
window.config(background='green')
window.title('Bomb')

# labels and entry boxes
headlabel = Label(window,text='Torture Bomb Game',font=('Arial',15,'bold'),background='black',fg='red')
headlabel.pack(fill=X,pady=10)
frame = LabelFrame(window)

label = Label(frame,text='Enter the range of count:',font=('Arial',12,'italic'))
label.grid(row=0,column=0,pady=10)

label1 = Entry(frame,font=('Arial',12,'italic'),width=8)
label1.grid(row=0,column=1,pady=10,padx=5)

msg = Label(frame,text='Enter the Message:',font=('Arial',12,'italic'))
msg.grid(row=1,column=0,pady=10)

msg1 = Entry(frame,font=('Arial',12,'italic'),width=8)
msg1.grid(row=1,column=1,pady=10,padx=5)

#Alert message with label
alert = Label(window)
alert.pack(fill=X)
msgg = Label(alert,text='Alert This Bomb use only for educational purpose',font=('Arial',9,'bold'),background='black',fg='red')
msgg.pack(pady=10)
frame.pack(pady=20)
#Button creation
bomb = Button(window,text='BOMB',font=('Arial',20,'bold'),fg='white',background='red',command=ok,activebackground='red')
bomb.pack(pady=10)
#Button bind with window in enter on tab
window.bind('<Return>','event generate %W <Tab>')

message = Frame(window)
mssg = Text(message,height=5,width=40,background='black',fg='green')
mssg.pack(fill=X)
message.pack()
#Auto run with text box in 0 , 1
for i in range(500):
    mssg.insert(END,0)
    mssg.insert(END,1)
# main program will run with this body of the loop
window.mainloop()
