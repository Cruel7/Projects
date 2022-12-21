#twosum
class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for x in range(i+1,len(nums)):
                if nums[i] + nums[x] == target:
                           return i,x

#test=Solution()
#print(test.twoSum(nums=[2,7,11,16],target=9))

#different solution
def find_indices():
    premap = {}
    for i,x in enumerate([1,2,3,4,5,6,8,1]):
        di=7-x
        if di in premap:
            return [premap[di],i]
        premap[x]=i
print(find_indices())

#accumulate numbers in a list
import itertools
def rs(nums):
    return itertools.accumulate(nums)
print(list(rs([1,2,3,4])))

#find pivot text
class xxx:
    def pivotIndex(self, nums: list[int]) -> int:
        total= sum(nums)
        temp = 0
        for i in range(len(nums)):
            if(nums[i] == total - 2*temp):
                return i
            temp += nums[i]
        return -1
x=xxx()
print(x.pivotIndex([1,2,3,3,4,4,5]))

#sum of 1D array
class SD:
    def runningSum(sef,nums):
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result

s=SD()
s.runningSum([1,2,3,4])

#isomorphic

def morph2(a,s):
    return len(set(zip(a,s)))==len(set(a)) and len(set(zip(s,a)))==len(set(s))
print(morph2("zzd","xxl"))

#subsequence
class Solution3:
    def isSubsequence(self, s, t):
        for i in range(0, len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
            t = t[index+1:]
        return True
dd=Solution3()
print(dd.isSubsequence(s="abc",t="asbscs"))

d="abc"
e="asbscs"
f=[]
for char in d:
    if char in e:
        f.append(d)
for x,i in enumerate(d):
    print(x,i)

xd=[1,5,3,4]
xdd=[4,5,8,6,7]
xf=xd+xdd
print(sorted(xf))


class Solution4():
    def mergeTwoLists(self, list1, list2):
        self.lf=list1+list2
        print(sorted(self.lf))
s=Solution4()
s.mergeTwoLists(list1=[1,2,4],list2=[1,3,4])

class Solution5():
    def reverseList(self,list3):
        list3.reverse()
        print(list3)

xds=Solution5()
xds.reverseList(list3=[1,2,3,4,5])

xdd.reverse()
print(xdd)

import statistics
from decimal import *

def tryx():
    if len(xdd)/2!=0:
        print(statistics.median(xdd))
    else:
        fx=round(len(xdd)/2)
        print(fx)

tryx()

#best time to buy
class Solution8:
    def maxProfit(self, prices):
        minPrice, highest = float('inf'), 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > highest:
                highest = price - minPrice
        return highest
ew=Solution8()
print(ew.maxProfit(prices=[7,1,3,5,6,4]))

class Sd:
    def maxpr(self,pr):
        mpr,hgh=float("inf"),0
        for price in pr:
            if price<mpr:
                mpr=price
            if price-mpr>hgh:
                hgh=price-mpr
        return hgh
er=Sd()
print(er.maxpr([11,2,35,7,86]))

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

pa=Palindr("dd")

class Solution4:
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

pas=Solution4(dd="abccccdd")

#duplicate
def duplicate():
    dupl=set()
    for x in [1,2,3,4,5,6,2,3,5,6]:
        if x in dupl:
            return True
        dupl.add(x)
        print(dupl)
    return False

print(duplicate())

xxxx=itertools.product([1,2,3,4,5])
print(list(xxxx))



def sumss():
    nums = [1, 2, 3, 4, -2, 3, 9, -1]
    maxs = nums[0]
    cursum = 0
    for x in nums:
        if cursum<0:
            cursum=0
        cursum+=x
        maxs=max(maxs,cursum)
    return maxs

print(sumss())

class Sd:
    def maxpr(self,pr):
        mpr,hgh=float("inf"),0
        for price in pr:
            if price<mpr:
                mpr=price
            if price-mpr>hgh:
                hgh=price-mpr
        return hgh
er=Sd()
print(er.maxpr([11,2,35,7,86]))

prices=[11,23,4,5,6,23,10]
def max_price():
    maxprice,highest=float("inf"),0
    for price in prices:
        if price<maxprice:
            maxprice=price
        if price-maxprice>highest:
            highest=price-maxprice
    return highest
print(max_price())

exp=itertools.product("abc",range(3))
print(list(exp))


def acc(nums):
    return itertools.accumulate(nums)

print(list(acc(prices)))

def it():
    for x in prices:
        yield (x)

print(sum(it()))