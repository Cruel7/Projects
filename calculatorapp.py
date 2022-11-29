from tkinter import *

root=Tk()
root.title("Calculator 1.0")
#input box
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def button_add(number):
    #e.delete(0, END)
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_pluss():
    first_number=e.get()
    global x
    global math
    math="addition"
    x=int(first_number)
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0,x + int(second_number))
    if math=="subtraction":
        e.insert(0,x - int(second_number))
    if math=="multiplication":
        e.insert(0,x * int(second_number))
    if math=="division":
        e.insert(0,x / int(second_number))

def button_min():
    first_number=e.get()
    global x
    global math
    math="subtraction"
    x=int(first_number)
    e.delete(0, END)
def button_mul():
    first_number=e.get()
    global x
    global math
    math="multiplication"
    x=int(first_number)
    e.delete(0, END)

def button_div():
    first_number=e.get()
    global x
    global math
    math="division"
    x=int(first_number)
    e.delete(0, END)

button1=Button(root, text="1",padx=40,pady=20,command=lambda: button_add(1))
button2=Button(root, text="2",padx=40,pady=20,command=lambda: button_add(2))
button3=Button(root, text="3",padx=40,pady=20,command=lambda: button_add(3))
button4=Button(root, text="4",padx=40,pady=20,command=lambda: button_add(4))
button5=Button(root, text="5",padx=40,pady=20,command=lambda: button_add(5))
button6=Button(root, text="6",padx=40,pady=20,command=lambda: button_add(6))
button7=Button(root, text="7",padx=40,pady=20,command=lambda: button_add(7))
button8=Button(root, text="8",padx=40,pady=20,command=lambda: button_add(8))
button9=Button(root, text="9",padx=40,pady=20,command=lambda: button_add(9))
button0=Button(root, text="0",padx=40,pady=20,command=lambda: button_add(0))
button_plus=Button(root,text="+",padx=40,pady=20,command=button_pluss)
button_equals=Button(root,text="=",padx=130,pady=20,command=button_equal)
button_clear=Button(root,text="C",padx=40,pady=20,command=button_clear)
button_minus=Button(root,text="-",padx=40,pady=20,command=button_min)
button_multi=Button(root,text="*",padx=40,pady=20,command=button_mul)
button_divide=Button(root,text="/",padx=40,pady=20,command=button_div)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=1)
button_plus.grid(row=4,column=0)
button_minus.grid(row=5,column=0)
button_multi.grid(row=4,column=2)
button_divide.grid(row=5,column=2)
button_equals.grid(row=6,columnspan=3)
button_clear.grid(row=5,column=1)
root.mainloop()