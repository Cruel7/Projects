#list comprehension
square=[i**2 for i in range(5) if i%2==0]
print(square)

#print all arguments
print(*square)

#days left
import datetime
d=datetime.date.today()-datetime.date(2022,12,31)
print(d)

#reverse list and palindrome
l1="1 2 4 4 2 1"
l2=[1,2,3,4,5,6]
print(l1==l1[::-1])

#multiple assignment
a,b,c=1,2,3
print(c,b,a)

#integer list
print(list(map(int,l1.split())))
print(list(map(int,l2)))

#reading file into a list
#names=[line.strip() for line in open("C://Users...,"r"")]

#unpacking
tup=(1,2,3,4,5)
lst=[1,2,3,4,5]
string="hello"
dic={"a":1,"b":2}
coords=[4,5]
a,b=dic.values()
#a,b,c,d,e=string
print(a,b)
print(type(a))
x,y=coords
print(x,y)

#nested list comprehension #use _ to substitute the i
x=[[i for i in range(5)] for i in range(3)]
print(x)

#count occuring instances from a string with a set
sen="Hi im GG"
x2={char:sen.count(char) for char in set(sen)}
print(x2)

sen2="ADSgdgd".lower()
x3={xd:sen2.count(xd) for xd in set(sen2)}
print(x3)
#zip
x5=(list(zip(lst,string)))

#kwargs
def func2(xw=None,bw=None,cw=None):
    print(xw,bw,cw)
kwargs={"bw":23,"xw":24,"cw":25}
func2(**kwargs)

#for else while loop
search=[1,2,3,4,5,6,7]
target=7
found=False
for elem in search:
    if elem==target:
        print("Done")
        found=True
        break
if not found:
    print("I didn't find it")

#sort by key
lstt=[[1,2],[3,4],[9,10],[7,8]]
lstt.sort(reverse=True)
print(lstt)

lstt.sort(key=lambda x: x[1]+x[0])
print(lstt)

#iterate with itertools
import itertools
kkg=[1,34,6,7,8]
kkg2=[123,4,5]
skkg=list(itertools.accumulate(kkg))
print(skkg)
chn=list(itertools.chain(kkg,kkg2))
print(chn)

lst23=[12,3,42,5,67,77]

#take random word from eng dictionary and convert

import random
from english_words import english_words_set
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
#map conversion to str
rword=random.sample([i for i in english_words_set if len(i)<8],1)
rword2=map(str,rword)
finalword= "".join(rword2)
print(finalword.lower())

###tkinter###
from tkinter import *
def tkbutton():
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


#pillow
from tkinter import *
def pillowimage():
    from PIL import ImageTk, Image
    root = Tk()
    root.title("Frames")
    frame = LabelFrame(root, text="This is a frame", pady=5, padx=5)
    frame.pack(padx=100, pady=100)

    b = Button(frame, text="Click here")
    b2 = Button(frame, text="Click here2")
    b.grid(row=0, column=0)
    b2.grid(row=1, column=1)

    root.mainloop()

#enumerate random list
import random
def enu():
    list1=[random.randint(1,20) for x in range(5)]
    print(list1)
    print(max(list1))

    for i,x in enumerate(list1):
        print(i,x)

#enu()

#url shortener
import pyshorteners
def shorten():
    link=input("Link please: \n")
    short=pyshorteners.Shortener()
    x=short.tinyurl.short(link)
    print(f"Shortened link is:\n{x}")
#shorten()

#Lambda and list iteration
def lam():
    myl=[1,2,3,4,5]
    myl2=[(lambda x: x**2)(x) for x in range(10)]
    print(myl2)
    sq=[]
    for x in range(10):
        sq.append(x*x)
    print(sq)

#generator like list comprehension and sum
events =[("learn",5),("learn",10),("kek", 20)]
st=(event[1]for event in events if event[0]=="learn")
sm=sum(st)
print(sm)

#itertools
from itertools import islice
xddd=["asd",'sd','dsds','dsdsds','sdsdw']
first5=islice(xddd,3)
for x in first5:
    print(x)

data="ASDAGGADSD"
from itertools import pairwise
for pair in pairwise(data):
    print(pair[0],pair[1])

from itertools import takewhile
data2=[1,2,3,4,5,-2,3,4]
items=takewhile(lambda x: x>0, data2)
for x in items:
    print(x)

