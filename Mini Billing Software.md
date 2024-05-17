from tkinter import *
from tkinter import  messagebox
def ok():
    if namEntry.get().lower() == 'admin' and pwdEntry.get().lower() == 'admin':
        messagebox.showinfo("Successfully","Succesfully Submited")
#------------------------------------------------------------------------------------
        import random,os
        from playsound import playsound
        billnumber=random.randint(1000,10000)
            
        def search_bill():
            for i in os.listdir('bills/'):
                if i.split('.')[0]==billEntry.get():
                    f = open(f'bills/{i}','r')
                    textarea.delete(1.0,END)
                    for data in f:
                        textarea.insert(END,data)
                        f.close()
                        break
            else:
                messagebox.showerror('Error','Invalid Number')

        if not os.path.exists('bills'):
            os.mkdir('bills')

        
        def save_bill():
            global billnumber
            result= messagebox.askyesno('Confirm','Do you want save this bill')
            if result:
                bill_content = textarea.get(1.0,END)
                file=open(f'bills/{billnumber}.txt','w')
                file.write(bill_content)
                file.close()
                messagebox.showinfo('Success',f'Bill number{bill_content} is saved successfully')
        def billing():
            billing.get()
        #----------------------------------------------------------------------------------------------------------------------------------------------
        def bill_area():
            if nameEntry.get() =="" or phoneEntry.get() =="":
                messagebox.showerror("Error","customer Details Are Required")
            elif burger_1Entry.get() == "" and pizza_1Entry.get() =="" and cooldrinks_1Entry =="":
                messagebox.showerror("Error","No product are Selected")
            elif burger_1Entry.get()=="0 Rs" and pizza_1Entry.get() == "0 Rs" and cooldrinks_1Entry.get() == "0 Rs":
                messagebox.showerror("Error","No product are Selected")
            else:
                textarea.delete(1.0,END)
                textarea.insert(END, "\t** Welcome KL Rahul Software **\n")
                textarea.insert(END,"\n--------------------------------------------\n")
                textarea.insert(END,f'Bill NUmber       : {billnumber}\n')
                textarea.insert(END,f'Customer Name     : {nameEntry.get()}\n')
                textarea.insert(END,f'Mobile Number     : {phoneEntry.get()}\n')
                textarea.insert(END,"\n--------------------------------------------\n")
                textarea.insert(END,"Products\t\tQty\tPrice\n")
                textarea.insert(END,"\n--------------------------------------------\n")
                if burger_1Entry.get()!='0':
                    textarea.insert(END,f'\nChicken Burger\t\t{burger_1Entry.get()}\t{burgerprice1}Rs')
                

                if burger_2Entry.get()!='0':
                    textarea.insert(END,f'\nEgg Burger\t\t{burger_2Entry.get()}\t{burgerprice2}Rs')
                    
                if burger_3Entry.get()!='0':
                    textarea.insert(END,f'\nVegg Burger\t\t{burger_3Entry.get()}\t{burgerprice3}Rs')
                    

                if burger_4Entry.get()!='0':
                    textarea.insert(END,f'\nMushroom Burger\t\t{burger_4Entry.get()}\t{burgerprice4}Rs')
                    

                if burger_5Entry.get()!='0':
                    textarea.insert(END,f'\nCheese Burger\t\t{burger_5Entry.get()}\t{burgerprice5}Rs')

                
                    
            #---------------------------------------------------------------------------------------------------------
                if pizza_1Entry.get()!='0':
                    textarea.insert(END,f'\nChicken Pizza\t\t{pizza_1Entry.get()}\t{pizzaprice1}Rs')
                    

                if pizza_2Entry.get()!='0':
                    textarea.insert(END,f'\nEgg Pizza\t\t{pizza_2Entry.get()}\t{pizzaprice2}Rs')
                    

                if pizza_3Entry.get()!='0':
                    textarea.insert(END,f'\nCheese Pizza\t\t{pizza_3Entry.get()}\t{pizzaprice3}Rs')
                    

                if pizza_4Entry.get()!='0':
                    textarea.insert(END,f'\nMushroom Pizza\t\t{pizza_4Entry.get()}\t{pizzaprice4}Rs')
                    

                if pizza_5Entry.get()!='0':
                    textarea.insert(END,f'\nVegg Pizza\t\t{pizza_5Entry.get()}\t{pizzaprice5}Rs')
                                
            #---------------------------------------------------------------------------------------------------------    
            #---------------------------------------------------------------------------------------------------------
                if cooldrinks_1Entry.get()!='0':
                    textarea.insert(END,f'\nMaaza\t\t{cooldrinks_1Entry.get()}\t{cooldrinksprice1}Rs')
                    

                if cooldrinks_2Entry.get()!='0':
                    textarea.insert(END,f'\n7 Up\t\t{cooldrinks_2Entry.get()}\t{cooldrinksprice2}Rs')
                    

                if cooldrinks_3Entry.get()!='0':
                    textarea.insert(END,f'\nMountainDew\t\t{cooldrinks_3Entry.get()}\t{cooldrinksprice3}Rs')


                if cooldrinks_4Entry.get()!='0':
                    textarea.insert(END,f'\nFanta\t\t{cooldrinks_4Entry.get()}\t{cooldrinksprice4}Rs')
                    

                if cooldrinks_5Entry.get()!='0':
                    textarea.insert(END,f'\nBovonto\t\t{cooldrinks_5Entry.get()}\t{cooldrinksprice5}Rs')
                    
                textarea.insert(END,"\n--------------------------------------------\n")  

                if burgertaxEntry.get()!='0.0 Rs':
                    textarea.insert(END,f'\n Burger Tax\t\t{burgertaxEntry.get()}')

                if pizzataxEntry.get()!='0.0 Rs':
                    textarea.insert(END,f'\n Pizza Tax\t\t{pizzataxEntry.get()}')
                
                if mstaxEntry.get()!='0.0 Rs':
                    textarea.insert(END,f'\n Burger Tax\t\t{mstaxEntry.get()}\n')

                textarea.insert(END,f'\n Total Bill \t\t{totalbill}')
                textarea.insert(END,"\n--------------------------------------------\n")  
                save_bill()
        #---------------------------------------------------------------------------------------------------------    



        # total button click to work  burger total amount
        def totalvalue():
            global totalbill
            global burgerprice1,burgerprice2,burgerprice3,burgerprice4,burgerprice5
            global pizzaprice1,pizzaprice2,pizzaprice3,pizzaprice4,pizzaprice5
            global cooldrinksprice1,cooldrinksprice2,cooldrinksprice3,cooldrinksprice4,cooldrinksprice5

            burgerprice1=int(burger_1Entry.get())*70  #chicken burger
            burgerprice2=int(burger_2Entry.get())*50  #Egg burger
            burgerprice3=int(burger_3Entry.get())*50  #veg burger
            burgerprice4=int(burger_4Entry.get())*50  #Mushroom burger
            burgerprice5=int(burger_5Entry.get())*50  #cheeshe burger

            totalburger_price = burgerprice1+burgerprice2+burgerprice3+burgerprice4+burgerprice5
            billmenuEntry.delete(0,END)
            billmenuEntry.insert(0,f'{totalburger_price} Rs')

            burgertax = totalburger_price * 0.12
            burgertaxEntry.delete(0,END)
            burgertaxEntry.insert(0,f'{burgertax} Rs')

        # pzza total amount to work
            
            pizzaprice1 =int(pizza_1Entry.get())*200
            pizzaprice2 =int(pizza_2Entry.get())*120
            pizzaprice3 =int(pizza_3Entry.get())*100
            pizzaprice4 =int(pizza_4Entry.get())*150
            pizzaprice5 =int(pizza_5Entry.get())*130

            totalpizzaprice = pizzaprice1+pizzaprice2+pizzaprice3+pizzaprice4+pizzaprice5
            billmenu_2Entry.delete(0,END)
            billmenu_2Entry.insert(0,str(totalpizzaprice)+"Rs")

            pizzatax = totalpizzaprice * 0.05
            pizzataxEntry.delete(0,END)
            pizzataxEntry.insert(0,str(pizzatax)+"Rs")

        # cool drinks ----------------------
        
            
            cooldrinksprice1 = int(cooldrinks_1Entry.get())*80
            cooldrinksprice2 = int(cooldrinks_2Entry.get())*80
            cooldrinksprice3 = int(cooldrinks_3Entry.get())*100
            cooldrinksprice4 = int(cooldrinks_4Entry.get())*80
            cooldrinksprice5 = int(cooldrinks_5Entry.get())*80

            totalcooldrinksprice = cooldrinksprice1+cooldrinksprice2+cooldrinksprice3+cooldrinksprice4+cooldrinksprice5
            billmenu_3Entry.delete(0,END)
            billmenu_3Entry.insert(0,str(totalcooldrinksprice)+"Rs")

            cooldrinkstax = totalpizzaprice * 0.08
            mstaxEntry.delete(0,END)
            mstaxEntry.insert(0,str(cooldrinkstax)+"Rs")


            totalbill = totalburger_price + totalpizzaprice + totalcooldrinksprice + burgertax + pizzatax + cooldrinkstax

            # tax convertion

            
        #-----------------------------------------------------------------------------------------------------------------------------------------------



        window=Tk()
        window.title("Kl Rahul")
        window.geometry("1320x700")
        

        #heading label in head
        headingLabel = Label(window,text="KL RAHUL Billing Software",font=("times of new roman",20,"bold"),fg="black",bg="#D3D3D3",bd=10,relief=GROOVE)
        headingLabel.pack(fill=X,pady=7)

        customerdetailFrame =LabelFrame(window,text="Customer Details",font=("times of new roman",20,"bold"),fg="black",bg="white",bd=7,relief=GROOVE)
        customerdetailFrame.pack(fill=X)

        name = Label(customerdetailFrame,text="Customer Name",font=("times of new roman",12,"bold"),bd=7,fg="black",bg="white")
        name.grid(row=0,column=0,pady=20)

        nameEntry = Entry(customerdetailFrame,font=("arial",12,"bold"),bd=7)
        nameEntry.grid(row=0,column=5,padx=15)

        phoneLabel = Label(customerdetailFrame,text="Phone Number",font=("times of new roman",12,"bold"),bd=7,bg="white",fg="black")
        phoneLabel.grid(row=0,column=6,padx=15)

        phoneEntry = Entry(customerdetailFrame,font=("arial",12,"bold"),bd=7)
        phoneEntry.grid(row=0,column=7,padx=15)

        billnoLabel = Label(customerdetailFrame,text="Bill No",font=("times of new roman",12,"bold"),bd=7,bg="white",fg="black")
        billnoLabel.grid(row=0,column=8,padx=15)

        billEntry = Entry(customerdetailFrame,font=("arial",12,"bold"),bd=3)
        billEntry.grid(row=0,column=9,padx=15)

        search = Button(customerdetailFrame,text="Search",font=("times of new roman",15,"bold"),bd=3,bg="blue",fg="white",command=search_bill)
        search.grid(row=0,column=18,padx=30)

        
        burgerFrame=Frame(window)
        burgerFrame.pack(pady=2,fill=X)


        # 1create burgerframe 

        burger_Frame=LabelFrame(burgerFrame,text="BURGER",font=("times of new roman",20,"bold"),fg="black",bd=9,relief=GROOVE)
        burger_Frame.grid(row=0,column=0)


        # 1) burger_1 creat label

        burger_1Label =Label(burger_Frame,text="Chicken Burger 70 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        burger_1Label.grid(row=0,column=0)


        # 1) burger_1entry page

        burger_1Entry=Entry(burger_Frame,font=("arial",10,"bold"),width=10,bd=5)
        burger_1Entry.grid(row=0,column=1,padx=10,pady=9)
        burger_1Entry.insert(0,0)

        # 2) burger_2 label

        burger2_Label=Label(burger_Frame,text="Egg Burger 50 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        burger2_Label.grid(row=1,column=0)

        # 2) burger_2 entry page

        burger_2Entry = Entry(burger_Frame,font=("arial",10,"bold"),width=10,bd=5)
        burger_2Entry.grid(row=1,column=1,padx=10,pady=9)
        burger_2Entry.insert(0,0)

        # 3) burger_3 label

        burger_3Label = Label(burger_Frame,text="Vegg Burger 50 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        burger_3Label.grid(row=3,column=0)

        # 3) burger_3 entry

        burger_3Entry = Entry(burger_Frame,font=("arias",10,"bold"),width=10,bd=5)
        burger_3Entry.grid(row=3,column=1,padx=10,pady=9)
        burger_3Entry.insert(0,0)
        # 4) burger_4 label


        burger_4Label = Label(burger_Frame,text="Mushroom Burger 50 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        burger_4Label.grid(row=4,column=0)

        # 4) burger_4 entry

        burger_4Entry = Entry(burger_Frame,font=("arias",10,"bold"),width=10,bd=5)
        burger_4Entry.grid(row=4,column=1,padx=10,pady=9)
        burger_4Entry.insert(0,0)
        # 5) burger_5 label

        burger_5Label = Label(burger_Frame,text="Cheese Burger 50 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        burger_5Label.grid(row=5,column=0)

        # 5) burger_5 entry

        burger_5Entry = Entry(burger_Frame,font=("arias",10,"bold"),width=10,bd=5)
        burger_5Entry.grid(row=5,column=1,padx=10,pady=9)
        burger_5Entry.insert(0,0)
        #  pizza frame create


        pizzaFrame = LabelFrame(burgerFrame,text="PIZZA",font=("times new roman",20,"bold"),fg="black",bd=10,relief=GROOVE)
        pizzaFrame.grid(row=0,column=1)

        # 1) pizza_1 chicken label

        pizza_1Label = Label(pizzaFrame,text="Cicken Pizza 200 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        pizza_1Label.grid(row=0,column=0,pady=2,padx=20,sticky='w')

        # 1) pizza label create entry

        pizza_1Entry = Entry(pizzaFrame,font=("arial",10,"bold"),width=10,bd=5)
        pizza_1Entry.grid(row=0,column=1,padx=10,pady=9)
        pizza_1Entry.insert(0,0)
        # 2) piza_2 label create for Egg pizza

        pizza_2Label = Label(pizzaFrame,text="Egg Pizza 120 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        pizza_2Label.grid(row=1,column=0,pady=2,padx=20,sticky='w')

        # 2) pizza_3 entry 

        pizza_2Entry = Entry(pizzaFrame,font=("arial",10,"bold"),width=10,bd=5)
        pizza_2Entry.grid(row=1,column=1,padx=10,pady=9)
        pizza_2Entry.insert(0,0)
        # 3) piza_3 label create for Egg pizza

        pizza_3Label = Label(pizzaFrame,text="Cheese Pizza 100 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        pizza_3Label.grid(row=3,column=0,pady=2,padx=20,sticky='w')

        # 3) pizza_3 entry 

        pizza_3Entry = Entry(pizzaFrame,font=("arial",10,"bold"),width=10,bd=5)
        pizza_3Entry.grid(row=3,column=1,padx=10,pady=9)
        pizza_3Entry.insert(0,0)
        # 4) pizza_4 label

        pizza_4Label = Label(pizzaFrame,text="Mushroom Pizza 150 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        pizza_4Label.grid(row=4,column=0,pady=2,padx=20,sticky='w')

        # 4) pizza_4 entry

        pizza_4Entry = Entry(pizzaFrame,font=("arial",10,"bold"),width=10,bd=5)
        pizza_4Entry.grid(row=4,column=1,padx=10,pady=9)
        pizza_4Entry.insert(0,0)
        # 5) pizza_4 label

        pizza_5Label = Label(pizzaFrame,text="Vegg Pizza 130 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        pizza_5Label.grid(row=5,column=0,pady=2,padx=20,sticky='w')

        # 5) pizza_4 entry

        pizza_5Entry = Entry(pizzaFrame,font=("arial",10,"bold"),width=10,bd=5)
        pizza_5Entry.grid(row=5,column=1,padx=10,pady=9)
        pizza_5Entry.insert(0,0)
        #  cooldrinks frame create

        cooldrinksFrame = LabelFrame(burgerFrame,text="COOL DRINKS",font=("times new roman",20,"bold"),fg="black",bd=10,relief=GROOVE)
        cooldrinksFrame.grid(row=0,column=2)

        # 1) cooldrinks_1Label create label

        cooldrinks_1Label = Label(cooldrinksFrame,text="Maaza 80 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        cooldrinks_1Label.grid(row=0,column=0,pady=2,padx=20,sticky='w')

        # 1) cooldrinks_1label create entry

        cooldrinks_1Entry = Entry(cooldrinksFrame,font=("arial",10,"bold"),width=10,bd=5)
        cooldrinks_1Entry.grid(row=0,column=1,padx=10,pady=9)
        cooldrinks_1Entry.insert(0,0)
        # 2) cooldrinks_2 label 

        cooldrinks_2Label = Label(cooldrinksFrame,text="7 up 80 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        cooldrinks_2Label.grid(row=1,column=0,pady=2,padx=20,sticky='w')

        # 2) coolddrinks_2 entry 

        cooldrinks_2Entry = Entry(cooldrinksFrame,font=("arial",10,"bold"),width=10,bd=5)
        cooldrinks_2Entry.grid(row=1,column=1,padx=10,pady=9)
        cooldrinks_2Entry.insert(0,0)
        # 3) cooldrinksd_3 label 

        cooldrinks_3Label = Label(cooldrinksFrame,text="Mountain Dew 100 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        cooldrinks_3Label.grid(row=3,column=0,pady=2,padx=20,sticky='w')

        # 3) cooldrinks_3 entry 

        cooldrinks_3Entry = Entry(cooldrinksFrame,font=("arial",10,"bold"),width=10,bd=5)
        cooldrinks_3Entry.grid(row=3,column=1,padx=10,pady=9)
        cooldrinks_3Entry.insert(0,0)
        # 4) cooldinks_4 label

        cooldrinks_4Label = Label(cooldrinksFrame,text="Fanta 80 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        cooldrinks_4Label.grid(row=4,column=0,pady=2,padx=20,sticky='w')

        # 4) cooldrinks_4 entry

        cooldrinks_4Entry = Entry(cooldrinksFrame,font=("arial",10,"bold"),width=10,bd=5)
        cooldrinks_4Entry.grid(row=4,column=1,padx=10,pady=9)
        cooldrinks_4Entry.insert(0,0)
        # 5) cooldrinks_5 label

        cooldrinks_5Label = Label(cooldrinksFrame,text="Bovonto 80 Rs/-",font=("times of new roman",10,"bold"),fg="black")
        cooldrinks_5Label.grid(row=5,column=0,pady=2,padx=20,sticky='w')

        # 5) cooldrinks_5 entry

        cooldrinks_5Entry = Entry(cooldrinksFrame,font=("arial",10,"bold"),width=10,bd=5)
        cooldrinks_5Entry.grid(row=5,column=1,padx=10,pady=9)
        cooldrinks_5Entry.insert(0,0)
        billFrame = Frame(burgerFrame,bd=8,relief=GROOVE)
        billFrame.grid(row=0,column=3,padx=5)

        billareaLabel = Label(billFrame,text="Bill Area",font=("times of new roman",15,"bold"),bd=7,relief=GROOVE)
        billareaLabel.pack()

        scroll = Scrollbar(billFrame,orient=VERTICAL)
        scroll.pack(side=RIGHT,fill=Y)
        textarea = Text(billFrame,height=14,width=45,yscrollcommand=scroll.set)
        textarea.pack()
        scroll.config(command=textarea.yview)


        billmenuFrame=LabelFrame(window,text="Bill Menu",font=("times of new roman",20,"bold"),fg="black",bd=9,relief=GROOVE,width=10,height=1)
        billmenuFrame.pack(fill=X,pady=5)

        # 1) bill menu label create

        billmenu_1Label =Label(billmenuFrame,text="Burger Price",font=("times of new roman",10,"bold"),fg="black",height=1)
        billmenu_1Label.grid(row=0,column=1)

        billmenuEntry = Entry(billmenuFrame,font=("arial",10,"bold"),width=10,bd=5)
        billmenuEntry.grid(row=0,column=2,padx=10,pady=9)

        billmenu_2Label =Label(billmenuFrame,text="Pizza Price",font=("times of new roman",10,"bold"),fg="black",height=1)
        billmenu_2Label.grid(row=1,column=1)

        billmenu_2Entry = Entry(billmenuFrame,font=("arial",10,"bold"),width=10,bd=5)
        billmenu_2Entry.grid(row=1,column=2,padx=10,pady=9)

        billmenu_3Label =Label(billmenuFrame,text="Milksshakes  Price",font=("times of new roman",10,"bold"),fg="black",height=1)
        billmenu_3Label.grid(row=3,column=1)

        billmenu_3Entry = Entry(billmenuFrame,font=("arial",10,"bold"),width=10,bd=5)
        billmenu_3Entry.grid(row=3,column=2,padx=10,pady=9)


        burgertax_1Label =Label(billmenuFrame,text="Burger Tax",font=("times of new roman",10,"bold"),fg="black",height=1)
        burgertax_1Label.grid(row=0,column=3)

        burgertaxEntry = Entry(billmenuFrame,font=("arial",10,"bold"),width=10,bd=5)
        burgertaxEntry.grid(row=0,column=4,padx=10,pady=9)

        pizzatax_1Label =Label(billmenuFrame,text="Pizza Tax",font=("times of new roman",10,"bold"),fg="black",height=1)
        pizzatax_1Label.grid(row=1,column=3)

        pizzataxEntry = Entry(billmenuFrame,font=("arial",10,"bold"),width=10,bd=5)
        pizzataxEntry.grid(row=1,column=4,padx=10,pady=9)

        mstax_1Label =Label(billmenuFrame,text="Milkshakes Tax",font=("times of new roman",10,"bold"),fg="black",height=1)
        mstax_1Label.grid(row=3,column=3,padx=10)

        mstaxEntry = Entry(billmenuFrame,font=("arial",10,"bold"),width=10,bd=5)
        mstaxEntry.grid(row=3,column=4,padx=40,pady=9)

        buttonFrame = Frame(billmenuFrame,relief=GROOVE)
        buttonFrame.grid(row=0,column=4,rowspan=3)

        totalButtonFrame=Button(billmenuFrame,text="Total",font=("arial",16,"bold"),bg="blue",fg="white",bd=5,command=totalvalue)
        totalButtonFrame.grid(row=1,column=5,pady=10,padx=50)

        billButtonFrame=Button(billmenuFrame,text="  Bill  ",font=("arial",16,"bold"),bg="red",fg="white",bd=5,command=bill_area)
        billButtonFrame.grid(row=1,column=6,pady=10,padx=50)

        printButtonFrame=Button(billmenuFrame,text="Print",font=("arial",16,"bold"),bg="green",fg="white",bd=5,command=save_bill)
        printButtonFrame.grid(row=1,column=7,pady=10,padx=50)

        window.mainloop()
    else:
        messagebox.showerror("Error","User name and password will not correct!...")    
#------------------------------------------------------------------------------------





root = Tk()
root.geometry("500x300")
headinglabel = Label(root,text="Login Kl Rahul Software",fg="black",font=("times of new roman",30,"bold"),bg="light grey")
headinglabel.pack(fill=X)
frame = Frame(root,bg="light pink",height=500,width=500)
frame.pack(fill=X,pady=10)

namlabel = Label(frame,text="Name  ",font=("times of new roman",15,"bold"),bg="light pink")
namlabel.grid(row=0,column=0,padx=10,pady=10)

namEntry = Entry(frame,font=("times of new roman",15,"bold"),relief=RIDGE)
namEntry.grid(row=0,column=1)

pwdlabel = Label(frame,text="Password", font=("times of new roman",15,"bold"),bg="light pink")
pwdlabel.grid(row=1,column=0,padx=5,pady=5)

pwdEntry = Entry(frame,font=("times of new roman",15,"bold"),relief=RIDGE)
pwdEntry.grid(row=1,column=1)

btn = Button(frame,text="Submit",font=("times of new roman",15,"bold"),relief=RIDGE,height=1,width=12,command=ok)
btn.grid(row=3,column=1,pady=50)
    
root.mainloop()
