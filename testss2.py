from english_words import english_words_set
import random
import warnings
warnings.simplefilter(action='ignore', category=DeprecationWarning)
randword=random.sample([i for i in english_words_set if len(i) < 8], 1)
randword2=map(str, randword)
finalword= "".join(randword2).lower().strip()
print(finalword)

class Palindr:
    def __init__(self,dd):
        stre=dd.lower()
        if stre[::-1]==stre:
            print("It's a palindrome")
        strel=(list(sorted(stre)))
        x=map(str,strel)
        finalx="".join(x)
        print(finalx)
        if finalx[::-1]==finalx:
            print("Also a palindrome after conversion")
        else:
            print("Not after conversion")

pa=Palindr(dd=finalword)

nums=[1,23,4,5,6,7,8]
target=23

if target in nums:
    print(f"{target} is in nums at position {nums.index(target)}")
else:
    print("-1")



class Solution2:
    def search(self):
        nums = [1, 23, 4, 5, 6, 7, 8]
        target = 23
        if target in nums:
            print(f"{target} is in nums at position {nums.index(target)}")
        else:
            print("-1")


s = Solution2()
s.search()

ver=[1,2,3,4,5,5.1,5.2,5.3,6.7]
cutoff=5.11
newv=[]
def lv():
    for i in ver:
        if i>cutoff:
            newv.append(i)
lv()
print(f"First bad version is {newv[0]}")


import itertools
def rs(nums):
    return itertools.accumulate(nums)
print(list(rs([1,2,3,4])))


def find_indices():
    premap = {}
    for i,x in enumerate([1,2,3,4,5,6,8,1]):
        di=7-x
        if di in premap:
            return [premap[di],i]
        premap[x]=i
print(find_indices())