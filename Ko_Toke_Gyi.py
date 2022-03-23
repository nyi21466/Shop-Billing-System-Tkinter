from tkinter import *
from tkinter import messagebox
from time import strftime
from prettytable import PrettyTable
s = Tk()
s.title('Ko Toke Gyi Bussiness')
s.geometry('1350x700')
s.configure(bg="black")

def sub():
      global T1     
      prices = "Rice = ," + str (E7.get())+","+"Peal De Sein = ," + str (E8.get())+","+"Fried Peas = ," +str (E9.get())+","+"Egg = ," +str (E10.get())
    
      today = strftime("%Y" + "." + "%m" + "." + "%d")
      direction ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\Daily Price\price"+ str(today) +".txt"
      a = open(direction,"w")
      a.write(prices)
      a.close()
      E7.delete(0,END)
      E8.delete(0,END)
      E9.delete(0,END)
      E10.delete(0,END)
      T1.withdraw()
  
def CGP():
    global T1
    T1.deiconify()
    
def hidethis():
    global T1
    T1.withdraw()
  
def CP():
    today = strftime("%Y" + "." + "%m" + "." + "%d")
    direction ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\Daily Price\price"+ str(today) +".txt"
    a = open(direction,"r")
    b = a.read()
    result = b.split(",")
    a.close()
    
    T2 = Toplevel(s,height = 600,width = 700,bg = "lightblue")
    T2.title("Prices")
    L11 = Label(T2, text="Rice = " + result[1],font ="Time 20",bg ="black",fg="red",height=1,width=18,relief=RAISED,bd=7)
    L11.place( x = 40, y = 50 )
    
    L12 = Label(T2, text="Peal De sein = "+ result[3],font ="Time 20",bg ="black",fg="red",height=1,width=18,relief=RAISED,bd=7)
    L12.place( x = 40, y = 120 )
    
    L13 = Label(T2, text="Fried peas = "+ result[5],font ="Time 20",bg ="black",fg="red",height=1,width=18,relief=RAISED,bd=7)
    L13.place( x = 350, y = 50)
    
    L14 = Label(T2, text="Egg = "+ result[7],font ="Time 20",bg ="black",fg="red",height=1,width=18,relief=RAISED,bd=7)
    L14.place( x = 350, y = 120)
    
def GB():
    global showvoucher
    global table
    global subtotal
    global taxes
    global total
    global buy1
    global buy2
    global buy3
    global buy4
    buy1 = 0
    buy2 = 0
    buy3 = 0
    buy4 = 0
    showvoucher = ""
    showvoucher += '-----------------Ko Toke Gyi Bussiness-----------------\n\n'
    # date time vou number cus details
    table = PrettyTable(['Item Name', 'Quantity', 'Unit Price', 'Item Price'])
    subtotal = ""
    taxes = ""
    total = ""
    ricetotal = 0
    pealtotal = 0
    peastotal = 0
    eggtotal = 0

    today = strftime("%Y" + "." + "%m" + "." + "%d")
    direction ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\Daily Price\price"+ str(today) +".txt"
    a = open(direction,"r")
    b = a.read()
    result = b.split(",")
    a.close()
    
    indirection ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\inventory\\inventory.txt"
    c = open(indirection,"r")
    d = c.read()
    inresult = d.split(",")
    c.close()
    
    if var1.get() == 1 and E3.get() != "":
        if int(inresult[1]) >= int(E3.get()):
            ricetotal = int(E3.get())*int(result[1])
            table.add_row([ "Rice", E3.get() , result[1] , ricetotal ])
            buy1 = 1
        else:
            messagebox.showinfo("Inventory info","Not enough Rice in inventory\n               OR\n          Out of stock\n\n Please check inventory!")
    if var2.get() == 1 and E4.get() != "":
        if int(inresult[3]) >= int(E4.get()):
            pealtotal = int(E4.get())*int(result[3])
            table.add_row([ "Peal de sein", E4.get() , result[3] , pealtotal ])
            buy2 = 1
        else:
            messagebox.showinfo("Inventory info","Not enough Peal in inventory\n               OR\n          Out of stock\n\n Please check inventory!")
    if var3.get() == 1 and E5.get() != "":
        if int(inresult[5]) >= int(E5.get()):
            peastotal = int(E5.get())*int(result[5])
            table.add_row([ "Fried peas", E5.get() , result[5] , peastotal ])
            buy3 = 1
        else:
            messagebox.showinfo("Inventory info","Not enough Fried peas in inventory\n               OR\n          Out of stock\n\n Please check inventory!")
    if var4.get() == 1 and E6.get() != "":
        if int(inresult[7]) >= int(E6.get()):
            eggtotal = int(E6.get())*int(result[7])
            table.add_row([ "Egg", E6.get() , result[7] , eggtotal ])
            buy4 = 1
        else:
            messagebox.showinfo("Inventory info","Not enough Egg in inventory\n               OR\n          Out of stock\n\n Please check inventory!")
    
    subtotal = ricetotal + pealtotal + peastotal + eggtotal
    taxes = subtotal / 100
    total = subtotal + taxes

    table.add_row(["----------", "----------", "----------", "----------"])    
    table.add_row(['','','SUBTOTAL', subtotal])
    table.add_row(["", "", "----------", "----------"])    
    table.add_row(['','','Taxes', taxes])
    table.add_row(["", "", "----------", "----------"])    
    table.add_row(['','','TOTAL', total])
    showvoucher += str(table)
    
    if E1.get() != "":
        pay = E1.get()
        pyanearn = int(pay) - total
        LPE.config ( text = str(pyanearn) )
        showvoucher += '\n\nYour pay money is ' + pay + ' kyat.\n'
        showvoucher += 'Our pyanearn money is ' + str(pyanearn) + ' kyat.'
    
    
    
    showvoucher += '\n\nThanks for shopping with us. \n'
    showvoucher += 'Your total bill amount is  ' + str(total) + ' Kyat.'
    
    M1.config( text = showvoucher )
    L2.config( text ="Sub Total = " + str(subtotal) )
    L3.config( text ="Taxes       = " + str(taxes) )
    L4.config( text ="Total        = " + str(total) )

def add(item):    
    indirection ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\inventory\\inventory.txt"
    c = open(indirection,"r")
    d = c.read()
    inresult = d.split(",")
    c.close()
    
    if item == "1" and E11.get() != "":
        inresult[1] = int(inresult[1]) + int(E11.get())
        E11.delete(0,END)
    if item == "2" and E12.get() != "":
        inresult[3] = int(inresult[3]) + int(E12.get())
        E12.delete(0,END)
    if item == "3" and E13.get() != "":
        inresult[5] = int(inresult[5]) + int(E13.get())
        E13.delete(0,END)
    if item == "4" and E14.get() != "":
        inresult[7] = int(inresult[7]) + int(E14.get())
        E14.delete(0,END)
    
    instock = "Rice = ," + str (inresult[1])+","+"Peal De Sein = ," + str (inresult[3])+","+"Fried Peas = ," +str (inresult[5])+","+"Egg = ," +str (inresult[7])
    
    c = open(indirection,"w")
    c.write(instock)
    c.close()
    
    c = open(indirection,"r")
    d = c.read()
    inresult = d.split(",")
    c.close()
    
    L15.config( text="Rice = "+ inresult[1] )
    L16.config( text="Peal De sein = "+ inresult[3] )
    L17.config( text="Fried peas = "+ inresult[5] )
    L18.config( text="Egg = "+ inresult[7] )
 
def IV():
    global T3
    T3.deiconify()
    
def hideT3():
    global T3
    T3.withdraw()

def Print():
    global buy1
    global buy2
    global buy3
    global buy4
    global showvoucher
    global table
    global subtotal
    global taxes
    global total
    
    indirection ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\inventory\\inventory.txt"
    c = open(indirection,"r")
    d = c.read()
    inresult = d.split(",")
    c.close()    
    
    if total != "" and subtotal != 0:
        currenttime = strftime("%Y" + "." + "%m" + "." + "%d" + "." + "%H"+ "." + "%M"+ "." + "%S")
        direction ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\vouchers\\voucher"+ str(currenttime) +".txt"
        a = open(direction,"w")
        a.write(showvoucher)
        a.close()
        if buy1 == 1:
            inresult[1] = int(inresult[1]) - int(E3.get())
        if buy2 == 1:
            inresult[3] = int(inresult[3]) - int(E4.get())
        if buy3 == 1:
            inresult[5] = int(inresult[5]) - int(E5.get())
        if buy4 == 1:
            inresult[7] = int(inresult[7]) - int(E6.get())
            
    instock = "Rice = ," + str (inresult[1])+","+"Peal De Sein = ," + str (inresult[3])+","+"Fried Peas = ," +str (inresult[5])+","+"Egg = ," +str (inresult[7])
    
    c = open(indirection,"w")
    c.write(instock)
    c.close()
    
    c = open(indirection,"r")
    d = c.read()
    inresult = d.split(",")
    c.close()
    
    L15.config( text="Rice = "+ inresult[1] )
    L16.config( text="Peal De sein = "+ inresult[3] )
    L17.config( text="Fried peas = "+ inresult[5] )
    L18.config( text="Egg = "+ inresult[7] )
    
    E1.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    # check button to state changes also available
    
    L2.config( text ="Sub Total = " )
    L3.config( text ="Taxes       = " )
    L4.config( text ="Total        = " )
    
    LPE.config ( text = "" )
    
    showvoucher = ""
    showvoucher += '-----------------Ko Toke Gyi Bussiness-----------------\n\n'
    # date time vou number cus details
    table = PrettyTable(['Item Name', 'Quantity', 'Unit Price', 'Item Price'])
    subtotal = ""
    taxes = ""
    total = ""

    table.add_row(["----------", "----------", "----------", "----------"])    
    table.add_row(['','','SUBTOTAL', subtotal])
    table.add_row(["", "", "----------", "----------"])    
    table.add_row(['','','Taxes', taxes])
    table.add_row(["", "", "----------", "----------"])    
    table.add_row(['','','TOTAL', total])
    showvoucher += str(table)
    showvoucher += '\n\nThanks for shopping with us. \n'
    showvoucher += 'Your total bill amount is  ' + str(subtotal) + ' Kyat.'
    
    M1.config( text = showvoucher )
    
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

TF = Frame(s,height = 60,width = 1290, bg = 'black',highlightbackground = "cyan",highlightthickness = 3)
TF.place(x=30,y=10)
L1 = Label(TF, text ="Ko Toke Gyi Bussiness", fg = 'white',bg = 'black' ,font = 'Times 25 bold', width = "62",justify = CENTER)
L1.place( x=0, y =0)
F1 = Frame(s,height = 450,width = 425, bg = 'black',highlightbackground = "red",highlightthickness = 3)
F1.place(x=30,y=80)
F2 = Frame(s,height = 450,width = 425, bg = 'black',highlightbackground = "red",highlightthickness = 3)
F2.place(x=462,y=80)
F3 = Frame(s,height = 450,width = 425, bg = 'white',relief = SUNKEN , bd = 5)
F3.place(x=895,y=80)
F4 = Frame(s,height = 150,width = 635, bg = 'black',highlightbackground = "red",highlightthickness = 3)
F4.place(x=30,y=540)
F5 = Frame(s,height = 150,width = 650, bg = 'black',highlightbackground = "red",highlightthickness = 3)
F5.place(x=670,y=540)

showvoucher = ""
showvoucher += '-----------------Ko Toke Gyi Bussiness-----------------\n\n'
# date time vou number cus details
table = PrettyTable(['Item Name', 'Quantity', 'Unit Price', 'Item Price'])
subtotal = ""
taxes = ""
total = ""

table.add_row(["----------", "----------", "----------", "----------"])    
table.add_row(['','','SUBTOTAL', subtotal])
table.add_row(["", "", "----------", "----------"])    
table.add_row(['','','Taxes', taxes])
table.add_row(["", "", "----------", "----------"])    
table.add_row(['','','TOTAL', total])
showvoucher += str(table)
showvoucher += '\n\nThanks for shopping with us. \n'
showvoucher += 'Your total bill amount is  ' + str(subtotal) + ' Kyat.'

M1 = Message(F3,text =showvoucher,font ="courier 9",bg ="white",fg="black",width =425,justify = LEFT, anchor = "nw")
M1.place(x=0,y=0)

B1 = Button(F4,text = "Check Price",font ="Times 15 bold",bg = "skyblue", fg = "black",command = CP,
            activebackground="lightblue",activeforeground="gray",width=10,relief=RAISED,bd=7)
B1.place(x=10,y= 8)
B2 = Button(F4,text = "Change Price",font ="Times 15 bold",command = CGP,bg = "red", fg = "black", activebackground="pink",activeforeground="gray",width=10,relief=RAISED,bd=7)
B2.place(x=10,y=85)
B3 = Button(F4,text = "Generate Bill",font ="Times 15 bold",bg = "green",command= GB, fg = "black", activebackground="lightblue",activeforeground="gray",width=10,relief=RAISED,bd=7)
B3.place(x=225,y=8)
B4 = Button(F4,text = "Inventory",font ="Times 15 bold",command = IV,bg = "red", fg = "black", activebackground="pink",activeforeground="gray",width=10,relief=RAISED,bd=7)
B4.place(x=225,y=85)
B5 = Button(F4,text = "Print",font ="Times 15 bold",bg = "green",command= Print, fg = "black", activebackground="lightblue",activeforeground="gray",width=10,relief=RAISED,bd=7)
B5.place(x=440,y=8)
B6 = Button(F4,text = "Exit",font ="Times 15 bold",bg = "white",command = s.destroy,justify = RIGHT ,fg = "black", activebackground="yellow",activeforeground="gray",width=10,bd=7)
B6.place(x=440,y=85)


L2 = Label(F5, text ="Sub Total = ", fg = 'white',bg = 'blue' ,width = 28,font = 'Times 15',anchor= "w")
L2.place( x=25, y =10)
L3 = Label(F5, text ="Taxes       = ", fg = 'white', bg = 'blue' ,width = 28,font = 'Times 15',anchor = "w")
L3.place( x=25, y =60)
L4 = Label(F5, text ="Total        = ", fg = 'white',bg = 'blue' ,width = 28,font = 'Times 15',anchor = "w")
L4.place( x=25, y =110)
L5 = Label(F5, text ="Pay Money ", fg = 'black',bg = 'orange' , height = 2,width = 14,font = 'Times 15',anchor= "w")
L5.place( x=350, y =10)
L6 = Label(F5, text ="Pyan Earn Money ", fg = 'black',bg = 'orange' ,height = 2,width = 14,font = 'Times 15',anchor= "w")
L6.place( x=350, y =85)
E1 = Entry(F5,font = "Times 15",width = 8,bg = "lightblue",fg = "black",bd = 10)
E1.place(x=520,y=10,height = 50)
LPE = Label(F5,font = "Times 15",width = 8,bg = "lightblue",fg = "black",bd = 10)
LPE.place(x=520,y=85,height = 50)

CB1 = Checkbutton(F1,text = "Rice",font = "Times 15",width = 11,bg = "tomato",fg = "black",anchor = "w",justify = LEFT,variable = var1)
CB1.place(x=10,y=10,height = 40)
CB2 = Checkbutton(F1,text = "Peal de sein",font = "Times 15",width = 11,bg = "tomato",anchor = "w",fg = "black",justify = LEFT,variable = var2)
CB2.place(x=10,y=70,height = 40)
E3 = Entry(F1,font = "Times 15",width = 10,bg = "lightblue",fg = "black",bd = 10)
E3.place(x=200,y=10,height = 50)
E4 = Entry(F1,font = "Times 15",width = 10,bg = "lightblue",fg = "black",bd = 10)
E4.place(x=200,y=70,height = 50)

CB3 = Checkbutton(F2,text = "Fried peas",font = "Times 15",width = 11,bg = "tomato",fg = "black",anchor = "w",justify = LEFT,variable = var3)
CB3.place(x=10,y=10,height = 40)
CB4 = Checkbutton(F2,text = "Egg",font = "Times 15",width = 11,bg = "tomato",anchor = "w",fg = "black",justify = LEFT,variable = var4)
CB4.place(x=10,y=70,height = 40)
E5 = Entry(F2,font = "Times 15",width = 10,bg = "lightblue",fg = "black",bd = 10)
E5.place(x=200,y=10,height = 50)
E6 = Entry(F2,font = "Times 15",width = 10,bg = "lightblue",fg = "black",bd = 10)
E6.place(x=200,y=70,height = 50)

T1 = Toplevel(s,height = 600,width = 700,bg = "lightblue")
T1.title("Prices")
L7 = Label(T1, text="Rice",font ="Time 20",bg ="black",fg="red",height=1,width=10,relief=RAISED,bd=7)
L7.place( x = 40, y = 20 )
E7 = Entry(T1,font = "Times 15",width = 10,bg = "white",fg = "black",bd = 10)
E7.place(x=220,y=20,height = 50)
L8 = Label(T1, text="Peal De sein",font ="Time 20",bg ="black",fg="red",height=1,width=10,relief=RAISED,bd=7)
L8.place( x = 40, y = 90 )
E8 = Entry(T1,font = "Times 15",width = 10,bg = "white",fg = "black",bd = 10)
E8.place(x=220,y=90,height = 50)
L9 = Label(T1, text="Fried peas",font ="Time 20",bg ="black",fg="red",height=1,width=10,relief=RAISED,bd=7)
L9.place( x = 350, y = 20 )
E9 = Entry(T1,font = "Times 15",width = 10,bg = "white",fg = "black",bd = 10)
E9.place(x=530,y=20,height = 50)
L10 = Label(T1, text="Egg",font ="Time 20",bg ="black",fg="red",height=1,width=10,relief=RAISED,bd=7)
L10.place( x = 350, y = 90)
E10 = Entry(T1,font = "Times 15",width = 10,bg = "white",fg = "black",bd = 10)
E10.place(x=530,y=90,height = 50)
B7 = Button(T1,text = "Submit",font ="Times 20 bold",command = sub,bg = "tomato", fg = "skyblue", activebackground="gray",activeforeground="skyblue")
B7.place(x=280,y=480)
T1.protocol("WM_DELETE_WINDOW", hidethis )
T1.withdraw()

T3 = Toplevel(s,height = 600,width = 700,bg = "lightblue")
T3.title("Inventory")

indirection ="C:\\Users\\Lenovo\\Desktop\\python software development\\tkinter gui exercises\\Shop billing system\\inventory\\inventory.txt"
c = open(indirection,"r")
d = c.read()
inresult = d.split(",")
c.close()
    
L15 = Label(T3, text="Rice = "+ inresult[1],font ="Time 15",bg ="black",fg="red",height=1,width=17,relief=RAISED,bd=7)
L15.place( x = 20, y = 20 )
E11 = Entry(T3,font = "Times 15",width = 5,bg = "white",fg = "black",bd = 10)
E11.place(x=220,y=20,height = 45)
B8 = Button(T3,text = "Add",font ="Times 15 bold",command = lambda:add("1"),bg = "black", fg = "white", activebackground="gray",activeforeground="skyblue")
B8.place(x=295,y=20)
L16 = Label(T3, text="Peal De sein = "+ inresult[3],font ="Time 15",bg ="black",fg="red",height=1,width=17,relief=RAISED,bd=7)
L16.place( x = 20, y = 80)
E12 = Entry(T3,font = "Times 15",width = 5,bg = "white",fg = "black",bd = 10)
E12.place(x=220,y=80,height = 45)
B9 = Button(T3,text = "Add",font ="Times 15 bold",command = lambda:add("2"),bg = "black", fg = "white", activebackground="gray",activeforeground="skyblue")
B9.place(x=295,y=80)
L17 = Label(T3, text="Fried peas = "+ inresult[5],font ="Time 15",bg ="black",fg="red",height=1,width=17,relief=RAISED,bd=7)
L17.place( x = 350, y = 20 )
E13 = Entry(T3,font = "Times 15",width = 5,bg = "white",fg = "black",bd = 10)
E13.place(x=550,y=20,height = 45)
B10 = Button(T3,text = "Add",font ="Times 15 bold",command = lambda:add("3"),bg = "black", fg = "white", activebackground="gray",activeforeground="skyblue")
B10.place(x=625,y=20)
L18 = Label(T3, text="Egg = "+ inresult[7],font ="Time 15",bg ="black",fg="red",height=1,width=17,relief=RAISED,bd=7)
L18.place( x = 350, y = 80)
E14 = Entry(T3,font = "Times 15",width = 5,bg = "white",fg = "black",bd = 10)
E14.place(x=550,y=80,height = 45)
B11 = Button(T3,text = "Add",font ="Times 15 bold",command = lambda:add("4"),bg = "black", fg = "white", activebackground="gray",activeforeground="skyblue")
B11.place(x=625,y=80)
T3.protocol("WM_DELETE_WINDOW", hideT3 )
T3.withdraw()
    
s.mainloop()

