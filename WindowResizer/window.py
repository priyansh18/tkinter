from tkinter import *

root = Tk()
root.title("Window Resizer on Input")

root.geometry(f"343x453") 

def getvals():
    print("Button Clicked")
    userwidth = widthvalue.get()
    userheight = heightvalue.get()
    root.geometry(f"{userwidth}x{userheight}") 


mylabel = Label(text="Welcome to Window Resizer : ",pady=20,padx=13)
mylabel.grid(row=0)

mywidth = Label(root,text="Width : ")
myheight = Label(root,text="Height : ")

mywidth.grid(row=1,column=0)
myheight.grid(row=2,column=0)

widthvalue = IntVar()
heightvalue = IntVar()

widthentry = Entry(root,textvariable=widthvalue).grid(row=1,column=1)
heightentry = Entry(root,textvariable=heightvalue).grid(row=2,column=1)

Button(text="Submit",command=getvals).grid(row=3,column=1,pady=20)



root.mainloop()