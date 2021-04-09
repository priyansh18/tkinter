from tkinter import *

from PIL import Image,ImageTk


priyansh_root = Tk()
priyansh_root.title("Image Displayer")


# Width x Height
priyansh_root.geometry("644x434")


# Width,height
priyansh_root.minsize(300,100)
priyansh_root.maxsize(1200,988)


# Important Label Options

title_label = Label(text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut \n labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco \n laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit \n in voluptate velit esse \n cillum dolore eu fugiat nulla pariatur.\n Excepteur sint occaecat cupidatat non proident,\n sunt in culpa qui officia deserunt mollit anim id est laborum.''',bg="red",fg="white",padx=23,pady=44,font=("comicsansms",19,"bold"),borderwidth=3,relief=SUNKEN)

# Important Pack Options
## anchor = nw--northwest
## side = top,bottom,left,right

# title_label.pack(side=BOTTOM,anchor="sw")
title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)


# # Adding Label

# mylabel = Label(text="Hello Friends,This is Priyansh Singhal")
# mylabel.pack()

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


# GUI Logic

priyansh_root.mainloop()