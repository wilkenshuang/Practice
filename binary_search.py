#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/6 15:23
# @Author  : Wilkenshuang
# @File    : test.py
# @Software: PyCharm Community Edition

List=[6, 8, 10, 11, 14, 15, 19, 25, 29, 33, 35, 36, 41, 42, 46, 47, 50, 61, 61, 69,70, 70, 82, 86, 87,
      91, 100, 104, 117, 118, 120, 121, 122, 131, 131, 133, 134, 136, 137, 141, 145, 148, 151, 153, 159,
      163, 164, 177, 177, 181, 182, 184, 190, 194, 197, 198, 198, 201, 206, 207, 209, 214, 215, 216, 218,
      221, 225, 226, 229, 230, 230, 231, 231, 232, 244, 249, 250, 256, 257, 257, 261, 269, 275, 278, 282,
      286, 289, 293, 295, 299, 301, 307, 307, 308, 315, 316, 316, 320, 322, 323, 323, 326, 328, 329, 331,
      333, 335, 340, 344, 346, 350, 351, 356, 361, 362, 369, 377, 380, 384, 385, 387, 395, 396, 396, 397]

def binary_search(n,test):
    low=0
    high=len(n)-1
    while low<high:
        mid=(low+high)//2
        mid_value=n[mid]
        if test>mid_value:
            low=mid+1
        elif test<mid_value:
            high=mid-1
        else:
            output=mid
            return output
    return None

output=binary_search(List,100)
print(List)
print(output)
print(List.index(100))
