from english_words import english_words_set
import random
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)

randword=random.sample([i for i in english_words_set if len(i) < 8], 1)
randword2=map(str, randword)
finalword= "".join(randword2).lower().strip()
#print(finalword)

def fun1():
    print(f"Welcome to Hangman. Try to guess the 8 or lower letter word. This one has {len(finalword)} letters")
    lettersguessed = ""
    lives = 6
    while lives>0:
        guess=input(" Guess a letter:\n").lower()
        if guess in finalword and len(guess)<2:
            print("Correct")
        elif len(guess)>=2:
            print("One letter max, try again")
            continue
        else:
            lives-=1
            print("Incorrect")
        lettersguessed=lettersguessed+guess
        print(f"Lives count is {lives}")

        wrongletter=0
        for letter in finalword:
            if letter in lettersguessed:
                print(f"{letter}",end="")
            else:
                print("_",end="")
                wrongletter+=1

        if wrongletter==0:
            print(f"\nYou win, the word is {finalword}")
            break
    else:
        print(f"\nYou lost, the word is {finalword}")

def fun2():
    q1=input("Want to play again? y/n")
    while True:
        if q1 not in ["y","n"]:
            print("Invalid input")
            q1=input("Want to play again? y/n")
            continue
        elif "y" in q1:
            fun1()
            fun2()
            break
        else:
            print("Thanks for playing")
            break

fun1()
fun2()
