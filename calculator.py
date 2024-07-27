from tkinter import *
equation = ""
def clear():
    global equation
    equation = ""
    label.config(text=equation)
def show(value):
    global equation
    equation+=value
    label.config(text=equation)
def calculate():
    global equation
    result=""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label.config(text=result)

window = Tk()
window.title("Calculator")
window.geometry('350x410')
window.iconbitmap('D://icon.ico')

heading = Label(window,text="CALCULATOR",font=("times of new roman",20,"bold"),fg="red",background="black")
heading.pack(fill=X)

label = Label(window,font=("times of new roman",30,"bold"),text="")
label.pack()

frame = Frame(window,background="black")
btn1 = Button(frame,text="1",font=("times of new roman",15,"bold"),width=7,command=lambda:show("1"),background="black",fg="white")
btn1.grid(row=0,column=0,padx=8,pady=3)

btn2 = Button(frame,text="2",font=("times of new roman",15,"bold"),width=7,command=lambda:show("2"),background="black",fg="white")
btn2.grid(row=0,column=1,padx=8,pady=3)

btn3 = Button(frame,text="3",font=("times of new roman",15,"bold"),width=7,command=lambda:show("3"),background="black",fg="white")
btn3.grid(row=0,column=3,padx=8,pady=3)

btn4 = Button(frame,text="4",font=("times of new roman",15,"bold"),width=7,command=lambda:show("4"),background="black",fg="white")
btn4.grid(row=1,column=0,padx=8,pady=3)

btn5 = Button(frame,text="5",font=("times of new roman",15,"bold"),width=7,command=lambda:show("5"),background="black",fg="white")
btn5.grid(row=1,column=1,padx=8,pady=3)

btn6 = Button(frame,text="6",font=("times of new roman",15,"bold"),width=7,command=lambda:show("6"),background="black",fg="white")
btn6.grid(row=1,column=3,padx=8,pady=3)

btn7 = Button(frame,text="7",font=("times of new roman",15,"bold"),width=7,command=lambda:show("7"),background="black",fg="white")
btn7.grid(row=2,column=0,padx=8,pady=3)

btn8 = Button(frame,text="8",font=("times of new roman",15,"bold"),width=7,command=lambda:show("8"),background="black",fg="white")
btn8.grid(row=2,column=1,padx=8,pady=3)

btn9 = Button(frame,text="9",font=("times of new roman",15,"bold"),width=7,command=lambda:show("9"),background="black",fg="white")
btn9.grid(row=2,column=3,padx=8,pady=3)

btn0 = Button(frame,text="0",font=("times of new roman",15,"bold"),width=7,command=lambda:show("0"),background="black",fg="white")
btn0.grid(row=3,column=0,padx=8,pady=3)

btn_plus = Button(frame,text="+",font=("times of new roman",15,"bold"),width=7,command=lambda:show("+"),background="black",fg="white")
btn_plus.grid(row=3,column=1,padx=8,pady=3)

btn_minus = Button(frame,text="-",font=("times of new roman",15,"bold"),width=7,command=lambda:show("-"),background="black",fg="white")
btn_minus.grid(row=3,column=3,padx=8,pady=3)

btn_mul = Button(frame,text="*",font=("times of new roman",15,"bold"),width=7,command=lambda:show("*"),background="black",fg="white")
btn_mul.grid(row=4,column=0,padx=8,pady=3)

btn_div = Button(frame,text="/",font=("times of new roman",15,"bold"),width=7,command=lambda:show("/"),background="black",fg="white")
btn_div.grid(row=4,column=1,padx=8,pady=3)

btn_clr = Button(frame,text="clear",font=("times of new roman",15,"bold"),width=7,command = lambda:clear(),background="orange",fg="black")
btn_clr.grid(row=4,column=3,padx=8,pady=3)

frame.pack(pady=10)
lbl = Label(window)
button_res = Button(window,text="=",font=("times of new roman",15,"bold"),width=27,command=lambda:calculate(),background="black",fg="white")
button_res.pack()
lbl.pack()
window.mainloop()
