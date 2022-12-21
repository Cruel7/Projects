import tkinter as tk


def fun1():
    window = tk.Tk()

    label = tk.Label(window, text="Little label:")
    label.pack()

    frame = tk.Frame(window, height=30, width=100, bg="#000099")
    frame.pack()

    button = tk.Button(window, text="Button")
    button.pack(fill=tk.X)

    switch = tk.IntVar()
    switch.set(1)

    checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
    checkbutton.pack()

    entry = tk.Entry(window, width=30)
    entry.pack()

    radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
    radiobutton_1.pack()
    radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
    radiobutton_2.pack()

    window.mainloop()


import tkinter as tk
from tkinter import messagebox

def xd():
    def click():
        tk.messagebox.showinfo("Click!", "I love clicks!")


    window = tk.Tk()
    label = tk.Label(window, text="Label")
    label.pack()

    button = tk.Button(window, text="Button", command=click)
    button.pack(fill=tk.X)

    frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
    frame.pack()

    window.mainloop()


def click1(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click1)   # Line I
label.pack()

button = tk.Button(window, text="Button", command=click1)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click1)   # Line II
frame.pack()

window.mainloop()
