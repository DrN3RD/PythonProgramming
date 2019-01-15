#stats.py

from math import *

def getNumbers():
    nums = [] #start with an empty list
    #Sentinel loop to get numbers

    xStr = input("Enter a number, <Enter to quit> ")

    while xStr != "":
        x = float(xStr)
        nums.append(xStr) #add this value to the list
        xStr = input("Enter a number, <Enter to quit> ")
    return nums

def mean(nums):

    total = 0.0
    for num in nums:

        total = total+float(num)
    return float(total/len(nums))

def stdDev(nums,xbar):

    sumDevSq = 0.0

    for num in nums:
        dev = float(num)-xbar
        sumDevSq = sumDevSq+(dev*dev)
    return sqrt(sumDevSq/(len(nums)-1))

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size//2
    if size % 2 ==0:
        med =(float(nums[midPos])+float(nums[midPos-1]))/2.0
    else:
        med = float(nums[midPos])
    return float(med)


def main():


    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data,xbar)
    med = median(data)

    print("\n The Mean is ",xbar)
    print("\n The Standard deviation is ", std)
    print("\n The Median is ", med)

if __name__ == '__main__': main()