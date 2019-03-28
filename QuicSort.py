# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:14:57 2019

@author: vanet
"""

import random
def partition(mylist, start, end, count):
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i],mylist[pos] = mylist[pos],mylist[i]
            pos += 1
    mylist[pos],mylist[end] = mylist[end],mylist[pos]
    return pos, count
def quicksort(mylist, start, end, count):
    if start < end:
        pos, count = partition(mylist, start, end, count)
        count = quicksort(mylist, start, pos - 1, count)
        count = quicksort(mylist, pos + 1, end, count)
    return count
x = [i for i in range(1000)]
random.shuffle(x)
count = quicksort(x, 0, len(x)-1, 0)
print(count)