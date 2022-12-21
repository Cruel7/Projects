import random
import time

mylist = [random.choice([x for x in range(15)]) for i in range(5)]
print(mylist)
mylist.sort(reverse=True)
print(mylist)
target = 3
time1 = time.time()


def exp():
    while True:
        if target not in mylist:
            print("Not in list")
            break
        else:
            occ = mylist.count(target)
            print(f"{target} is in position {mylist.index(target)}")
            print(f"Occurrences are {occ}")
            break


exp()


def locate():
    tries = 0
    low = 0
    high = len(mylist) - 1
    while low < high and target in mylist:
        mid = (low + high) // 2
        midnumber = mylist[mid]
        print(f"Low is {low}, high is {high}, mid is {mid}, middlenumber is {midnumber}")
        if midnumber == target:
            tries += 1
            print(f"Tries are {tries}")
            return mid

        elif midnumber > target:
            tries += 1
            high = mid - 1

        elif midnumber > target:
            tries += 1
            low = mid + 1
        else:
            print("Not in list")


locate()

myl = [1, 2, 3, 4, 5]
myl2 = [(lambda x: x ** 2)(x) for x in range(10)]
print(myl2)
for i, x in enumerate(myl2):
    print(i, x)
sq = []
for x in range(10):
    sq.append(x * x)
print(sq)

# reverse list and palindrome
l1 = "1 2 4 4 2 1"
l2 = [1, 2, 3, 4, 5, 6]
print(l1 == l1[::-1])

# multiple assignment
a, b, c = 1, 2, 3
print(c, b, a)

# integer list
print(list(map(int, l1.split())))
print(list(map(int, l2)))

# for else while loop
search = [1, 2, 3, 4, 5, 6, 7]
target = 7
found = False
for elem in search:
    if elem == target:
        print("Done")
        found = True
        break
if not found:
    print("I didn't find it")


def xxx():
    while True:
        if target not in search:
            print("Not found")
            break
        else:
            print("I found it")
            break


xxx()


def fullname():
    first = input("Enter name ")
    last = input("Enter surname ")
    print(f"The name is {first} {last}")


# fullname()
import pycodestyle
import autopep8


def hello(name: str) -> str:
    return "Hello, " + name


print(hello(name="G"))


def my_fun(a, b):
    """The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.
    """
    return a * b


print(my_fun.__doc__)
