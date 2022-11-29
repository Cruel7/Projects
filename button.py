from tkinter import *

root=Tk()
#input box
e=Entry(root,width=30,fg="blue")
e.pack()
e.insert(0,"Enter your name")

#click function
def Click():
    myLabel=Label(root,text=e.get())
    myLabel.pack()
#button settings
myButton=Button(root,text="Enter name",padx=25,pady=10,command=Click,fg="red")
myButton.pack()
myButton.mainloop()

e=Entry(root)
e.pack()