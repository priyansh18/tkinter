from tkinter import *
from PIL import Image,ImageTk


def every_100(text):
    final_text = ''
    for i in range(0,len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text +='\n'
    return final_text


root = Tk()
root.title("News")
root.geometry("3000x800")


texts = []
photos = []

## Getting All the Photos & Text file
for i in range(0,3):
    with open(f"{i+1}.txt",encoding="utf8") as f:
        text = f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.png")
    image = image.resize((125,165),Image.ANTIALIAS)
    # Resizing the Images
    photos.append(ImageTk.PhotoImage(image))


f0 = Frame(root,width=800,height=70)
Label(f0,text="News All Over The World",font="lucida 33 bold").pack()
Label(f0,text="April 12, 2021",font="lucida 13 bold").pack()
f0.pack()



f1 = Frame(root,width=900,height=200,pady=12)
Label(f1,text=texts[0],padx=22,pady=22).pack(side="left")
Label(f1,image=photos[0],anchor="e", pady=22).pack(side="left")
f1.pack(anchor="w")

f2 = Frame(root,width=900,height=200,pady=12)
Label(f2,text=texts[1],padx=22,pady=22).pack(side="right")
Label(f2,image=photos[1],anchor="w").pack(side="left")
f2.pack(anchor="w")

f2 = Frame(root,width=900,height=200,pady=12)
Label(f2,text=texts[2],padx=22,pady=22).pack(side="left")
Label(f2,image=photos[2],anchor="e").pack(side="left")
f2.pack(anchor="w")


root.mainloop()