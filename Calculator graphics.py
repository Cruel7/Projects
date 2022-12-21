from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Calculator 2.0")
#root.iconbitmap("location") for icon top left

#open image in TK
my_img= ImageTk.PhotoImage(Image.open("C:\\Users\\Monster\\Desktop\\Binance_jydPaXB8Wo.png"))
my_img1= ImageTk.PhotoImage(Image.open("C:\\Users\\Monster\\Desktop\\3710a0b1e7bd056eb478409b196418aa.png"))
my_img2= ImageTk.PhotoImage(Image.open("C:\\Users\\Monster\\Desktop\\Binance_xZ5I5XIVGd.png"))
my_img3= ImageTk.PhotoImage(Image.open("C:\\Users\\Monster\\Desktop\\IMG_5125.jpg"))

imagelist=[my_img,my_img1,my_img2,my_img3]

my_label=Label(image=my_img)
my_label.grid(row=0,column=0,columnspan=3)


def back(image_number):
    global my_label
    global button_back
    global button_fwd


def forward(image_number):
    global my_label
    global button_back
    global button_fwd
    my_label.grid_forget()
    my_label=Label(image=imagelist[image_number-1])
    button_fwd=Button(root,text="FWD", command=lambda: forward(image_number+1))
    button_back=Button(root,text="Back", command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_fwd.grid(row=1, column=2)
    button_back.grid(row=1, column=1)


button_back=Button(root,text="Back",command=back).grid(row=1,column=0)
button_fwd=Button(root,text="FWD",command=lambda: forward(2)).grid(row=1,column=2)
button_quit=Button(root,text="Exit Program", command=root.quit).grid(row=1,column=1)

root.mainloop()