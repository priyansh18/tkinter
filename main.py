from tkinter import *
import tkinter.messagebox as tsmg
from PIL import Image,ImageTk


# priyansh_root = Tk()
# priyansh_root.title("Image Displayer")

# 1 

# Width x Height
# priyansh_root.geometry("644x434")


# # Width,height
# priyansh_root.minsize(300,100)
# priyansh_root.maxsize(1200,988)

# 2

# # Adding Label

# mylabel = Label(text="Hello Friends,This is Priyansh Singhal")
# mylabel.pack()

# 3

# # Adding Image

# ## For Png Images

# photo = PhotoImage(file="1.png")
# alabel = Label(image=photo)
# alabel.pack()

# ### For JPG Images

# image = Image.open("2.jpg")
# aphoto = ImageTk.PhotoImage(image)
# blabel = Label(image=aphoto)
# blabel.pack()

# 4

# Important Label Options

# title_label = Label(text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut \n labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco \n laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit \n in voluptate velit esse \n cillum dolore eu fugiat nulla pariatur.\n Excepteur sint occaecat cupidatat non proident,\n sunt in culpa qui officia deserunt mollit anim id est laborum.''',bg="red",fg="white",padx=23,pady=44,font=("comicsansms",19,"bold"),borderwidth=3,relief=SUNKEN)

# Important Pack Options
## anchor = nw--northwest
## side = top,bottom,left,right

# title_label.pack(side=BOTTOM,anchor="sw")
# title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)

# 5

# # Frame 

# f1 = Frame(priyansh_root,bg="grey",borderwidth=7,relief=SUNKEN)
# f1.pack(side=LEFT,fill="y")

# f2 = Frame(priyansh_root,bg="grey",borderwidth=9,relief=SUNKEN)
# f2.pack(side=TOP,fill="x")


# l = Label(f1,text="Hello Friends")
# l.pack(pady=192)

# l = Label(f2,text="Welcome To Tkinter" ,font=("comicsansms",10,"bold"))
# l.pack(padx=192)

# 6 --- Packing Button in Tkinter

# def hello():
#     print("Hello Mate")

# def name():
#     print("My Name is Priyansh Singhal")

# f1 = Frame(priyansh_root,bg="grey",borderwidth=7,relief=SUNKEN)
# f1.pack(side=LEFT,anchor="nw")

# b1 = Button(f1,fg="red",text="Print Now",command=hello)
# b1.pack(side=LEFT,padx=20)

# b2 = Button(f1,fg="red",text="Tell me Your Name",command=name)
# b2.pack(side=LEFT,padx=20)

# b3 = Button(f1,fg="red",text="Print Now")
# b3.pack(side=LEFT,padx=20)

# b4 = Button(f1,fg="red",text="Print Now")
# b4.pack(side=LEFT,padx=20)

# 7 -- Entry Widget & Grid Layout

# def getvals():
#     print(uservalue.get())
#     print(passvalue.get())

# user = Label(priyansh_root,text="Username")
# password = Label(priyansh_root,text="Password")
# user.grid()
# password.grid(row=1)

# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(priyansh_root,textvariable=uservalue)
# passentry = Entry(priyansh_root,textvariable=passvalue)

# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)

# Button(text="Submit",command=getvals).grid()

# 8 -- Travel Forms using CheckButtons & Entry Widgets

# def getvals():
#     print("Submitting Form")
#     print(namevalue.get())
#     print(phonevalue.get())
#     print(gendervalue.get())
#     print(emergencyvalue.get())
#     print(paymentmodevalue.get())
#     print(foodservicevalue.get())
#     with open("records.txt","w") as f:
#         f.write(f"{namevalue.get() , phonevalue.get() , gendervalue.get() , emergencyvalue.get() , paymentmodevalue.get() , foodservicevalue.get()}\n")

# Label(priyansh_root,text="Welcome to Ghumakkar Travels",padx=32,font="comicsansms 13 bold").grid(row=0,column= 3)
# name = Label(priyansh_root,text="Name")
# phone = Label(priyansh_root,text="Phone")
# gender = Label(priyansh_root,text="Gender")
# emergency = Label(priyansh_root,text="Emergency Contact")
# paymentmode = Label(priyansh_root,text="Payment Mode")

# name.grid(row=1,column=2)
# phone.grid(row=2,column=2)
# gender.grid(row=3,column=2)
# emergency.grid(row=4,column=2)
# paymentmode.grid(row=5,column=2)

# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentmodevalue = StringVar()
# foodservicevalue = IntVar()

# nameentry = Entry(priyansh_root,textvariable=namevalue).grid(row=1,column=3)
# phoneentry = Entry(priyansh_root,textvariable=phonevalue).grid(row=2,column=3)
# genderentry = Entry(priyansh_root,textvariable=gendervalue).grid(row=3,column=3)
# emergencyentry = Entry(priyansh_root,textvariable=emergencyvalue).grid(row=4,column=3)
# paymentmodeentry = Entry(priyansh_root,textvariable=paymentmodevalue).grid(row=5,column=3)

# foodservice = Checkbutton(text="Want to get your meals ?",variable=foodservicevalue)
# foodservice.grid(row=6,column=3)

# Button(text="Submit to Ghumakkar Travels",command=getvals).grid(row=8,column=3)

# 9 -- Canvas Widget

# canvas_width = 800
# canvas_height = 400

# priyansh_root.geometry(f"{canvas_width}x{canvas_height}")
# can_widget = Canvas(priyansh_root,width=canvas_width,height=canvas_height)
# can_widget.pack()

# # the line goes from x1,y1 to x2,y2

# can_widget.create_line(0,0,800,400,fill="red")
# can_widget.create_line(0,400,800,0,fill="red")

# # the rectangle goes from top-left to bottom-right
# can_widget.create_rectangle(3,5,700,300,fill="blue")

# can_widget.create_text(200,200,text="python")

# 10 -- Handling Events 

# def myval(event):
#     print("Button Clicked")

# widget =  Button(priyansh_root,text="Click me please")
# widget.pack()

# widget.bind('<Button-1>',myval)
# widget.bind('<Double-1>', quit)


# 11 -- Menus & SubMenus

# ## Menu without Dropdown

# def myfunc():
#     print("My Name is Function I will only Execute If Someone Calls Me ....")

# def help():
#     print("I will help u")
#     tsmg.showinfo("help","I will help u  ")

# def rate():
#     print("Rate Us")
#     value = tsmg.askquestion("Was your Experience good ?","You used this GUI... was your Experience good ?")
#     print(value)
#     if value == "yes":
#         msg =  "Great. rate us on appstore please"
#     else:
#         msg = "Tell us what went wrong ? We will call you soon"
#     tsmg.showinfo("Experience",msg)


# # mymenu = Menu(priyansh_root)
# # mymenu.add_command(label="File",command = myfunc)
# # mymenu.add_command(label="Exit",command = quit)

# # priyansh_root.config(menu=mymenu)

# ## Menu with Dropdown

# mainmenu = Menu(priyansh_root)
# m1 = Menu(mainmenu,tearoff=0)
# m1.add_command(label="New project",command = myfunc)
# m1.add_command(label="Save",command = myfunc)
# m1.add_separator()
# m1.add_command(label="Save as",command = myfunc)
# m1.add_command(label="Print",command = myfunc)

# priyansh_root.config(menu = mainmenu)

# mainmenu.add_cascade(label="File",menu=m1)

# m2 = Menu(mainmenu,tearoff=0)
# m2.add_command(label="Cut",command = myfunc)
# m2.add_command(label="Copy",command = myfunc)
# m2.add_separator()
# m2.add_command(label="Paste",command = myfunc)
# m2.add_command(label="Find",command = myfunc)

# priyansh_root.config(menu = mainmenu)
# mainmenu.add_cascade(label="Edit",menu=m2)


# m3 = Menu(mainmenu,tearoff=0)
# m3.add_command(label="help",command = help)
# m3.add_command(label="rate us",command = rate)
# mainmenu.add_cascade(label="Help",menu=m3)
# priyansh_root.config(menu = mainmenu)

# 12 -- Sliders using Scale

# def getDollar():
#     print(f"We have credited {myslider.get()} dollars in your bank account")
#     tsmg.showinfo("Amount Credited",f"We have credited {myslider.get()} dollars in your bank account")

# Label(priyansh_root,text="How many dollars do you want ?").pack()
# myslider = Scale(priyansh_root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
# myslider.set(33)
# myslider.pack()

# Button(priyansh_root,text="Get Dollars!",pady=22,command=getDollar).pack()


# 13 -- Creating RadioButtons

# def order():
#     tsmg.showinfo("Order Received",f"We have received your order for {var.get()}.Thanks for Ordering")

# var = IntVar()
# Label(priyansh_root,text="What would you like to have sir ?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
# radio = Radiobutton(priyansh_root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
# radio = Radiobutton(priyansh_root,text="Idli",padx=14,variable=var,value=2).pack(anchor="w")
# radio = Radiobutton(priyansh_root,text="Wada",padx=14,variable=var,value=3).pack(anchor="w")
# radio = Radiobutton(priyansh_root,text="Samosa",padx=14,variable=var,value=4).pack(anchor="w")

# Button(text="Order Now",command=order).pack()

# 14 -- ListBox

# def add():
#     global i
#     lbx.insert(ACTIVE,f"{i}")
#     i+=1

# i=0
# lbx = Listbox(priyansh_root)
# lbx.pack()
# lbx.insert(END,"First Item of our Listbox")

# Button(priyansh_root,text="Add Item",command=add).pack()

# 15 -- ScrollBar
# scrollbar = Scrollbar(priyansh_root)
# scrollbar.pack(side=RIGHT,fill=Y)
# listbox = Listbox(priyansh_root,yscrollcommand=scrollbar.set )
# for i in range(344):
#     listbox.insert(END,f"Item {i}")

# scrollbar.config(command=listbox.yview)
# listbox.pack()


# 16 -- StatusBar

# def upload():
#     statusvar.set("Busy...")
#     sbar.update()
#     import time
#     time.sleep(2)
#     statusvar.set("Ready")

# statusvar = StringVar()
# statusvar.set("Ready")
# sbar = Label(priyansh_root,textvariable=statusvar,relief=SUNKEN,anchor="w")
# sbar.pack(side=BOTTOM,fill=X)
# Button(priyansh_root,text="Upload",command=upload).pack()

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar =  Label(self,textvar=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Button Clicked")

    def createButton(self,inptext):
        Button(text=inptext,command=self.click).pack()

if __name__ == "__main__":
    window = GUI()
    window.status()
    window.createButton("Click Me")
    window.mainloop()
# GUI Logic


# priyansh_root.mainloop()