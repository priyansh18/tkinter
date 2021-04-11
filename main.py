from tkinter import *

from PIL import Image,ImageTk


priyansh_root = Tk()
priyansh_root.title("Image Displayer")

# 1 

# Width x Height
priyansh_root.geometry("644x434")


# Width,height
priyansh_root.minsize(300,100)
priyansh_root.maxsize(1200,988)

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

def getvals():
    print(uservalue.get())
    print(passvalue.get())

user = Label(priyansh_root,text="Username")
password = Label(priyansh_root,text="Password")
user.grid()
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(priyansh_root,textvariable=uservalue)
passentry = Entry(priyansh_root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()




# GUI Logic

priyansh_root.mainloop()