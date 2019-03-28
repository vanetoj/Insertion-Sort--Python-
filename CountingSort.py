# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:13:00 2019

@author: vanet
"""

import numpy as np
counter=0

def counting_sort(array1, max_val):
    global counter
    m = max_val + 1
    count = [0] * m

    for a in array1:
        # count occurences
        count[a] += 1
        i = 0

    for a in range(m):
        counter+=1
        for c in range(count[a]):
            array1[i] = a
            i += 1
            counter+=1
    return array1



array1 = np.random.choice(1000, 1000, replace=True)
print (counting_sort(array1, 1000),counter)