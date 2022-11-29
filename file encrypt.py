di={1:"1",2:"2"}

di.update({"sd":"23",2:"24"})
print(di.keys(),di.values(),di.items())

import random
game=True

def fun1():
    options={"r":"rock","p":"paper","s":"scissors"}
    ch1=input("What do u choose?")

    while game:
        if ch1 not in options.keys():
            print("Invalid input")
            ch1=input("What do u choose")
            continue

        else:
            print(f"U've chosen {ch1}")
            break

    xd=["r","p","s"]
    ch2=random.choice(xd)

    print(f"I choose {ch2}")

    if ch1=="s" and ch2=="r":
        print(f"{ch2} wins")
    elif ch1=="s" and ch2=="p":
        print(f"{ch1} wins")
    elif ch1=="r" and ch2=="p":
        print(f"{ch2} wins")
    elif ch1=="r" and ch2 == "s":
        print(f"{ch1} wins")
    elif ch1=="p" and ch2=="s":
        print(f"{ch2} wins")
    elif ch1=="p" and ch2=="r":
        print(f"{ch1} wins")
    else:
        print("It's a tie!")

def fun2():
    mm = 0
    q1=input("Want to play again? y/n")
    while game:
        q1o=["y","n"]
        if q1 not in q1o:
            print("Read tardo")
            q1=input("Want to play again? y/n")
            continue
        elif "y" in q1:
            fun1()
            fun2()
            break
        else:
            print("GGs")
            break

fun1()
fun2()




