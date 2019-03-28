# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:05:54 2019

@author: vanet
"""

import random


def insertionSort(arr):

    numOfComp=0

# Traverse through 1 to len(arr)

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

    while j >= 0 and key < arr[j]:

        arr[j + 1] = arr[j]
        j -= 1
        numOfComp+=1

        print("The number of comparisons is : ", numOfComp)

        arr[j + 1] = key

# Driver code to test above

arr=[i for i in range(1000)]

random.shuffle(arr)

print(arr)

insertionSort(arr)

print("Sorted array is:")

for i in range(len(arr)):

    print("%d" % arr[i])