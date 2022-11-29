import winsound
def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

import time
dt=int(time.time())
print(int(dt))
sumd=sum(int(x) for x in str(dt))
print(sumd)



text = "Attack Alessia"
s = sumd

#print("Text  : " + text)
#print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))

game=True
tries=1
while game:
    q=int(input("pick the shift 1-100"))
    if q!=sumd:
        print("Naah lil bro")
        winsound.Beep(500,100)
        tries+=1
        continue
    else:
        print("U actually got it!")
        winsound.Beep(1000,2000)
        break

print(f"You did it in {tries} tries")
print("Text: " + text)