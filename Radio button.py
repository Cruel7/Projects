from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Radio Buttons")

#r=IntVar()
#r.set("2")

MODES=[
    ("Pep","Pep"),
    ("CH","CH"),
    ("TO","TO"),
    ("AV","AV"),
    ("SAL","SAL")
]

pizza=StringVar()
pizza.set("Pep")

for text,mode in MODES:
    Radiobutton(root, text=text, variable=pizza,value=mode).pack()


def clicked(value):
    mylabel=Label(root,text=value).pack()

#Radiobutton(root,text="Option 1", variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable=r,value=2,command=lambda: clicked(r.get())).pack()

mylabel=Label(root,text=pizza.get()).pack()

myButton=Button(root,text="Click me pls",command=lambda: clicked(pizza.get())).pack()


root.mainloop()
