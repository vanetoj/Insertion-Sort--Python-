# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:15:52 2019

@author: vanet
"""

import random
counter = 0


def merge_sort(lst):
    global counter
    if len(lst) <= 1:
        counter += 1 # increment counter when we dividing array on two
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    global counter
    if not left:
        counter += 1 # increment counter when not left (not left - is also comparison)
        return right
    if not right:
        counter += 1 # the same as above for right
        return left
    if left[0] < right[0]:
        counter += 1 # and the final one increment
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


lst =[i for i in range(998)]
random.shuffle(lst)

# also you don't need to return counter since you are using global value
print(merge_sort(lst), counter)
		