#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 20:47
# @Author  : Wilkenshuang
# @File    : test.py
# @Software: PyCharm Community Edition

'''
利用D&C思想（分而治之）来有小到大快速排列列表内的所有数。
用python自带的函数sorted（）或X.sort（）也能完成
input：[99,43,56,21,19,77]
output：[19, 21, 43, 56, 77, 99]
'''

def quickSort(list):
    if len(list)<2:
        return list
    else:
        pivot=list[0]
        subLeft,subRight=[],[]
        for i in list[1:]:
            if i<=pivot:
                subLeft.append(i)
            else:
                subRight.append(i)
        if len(subLeft)<=1:
            return subLeft + [pivot] +quickSort(subRight)
        elif len(subRight)<=1:
            return quickSort(subLeft) + [pivot] + subRight
        else:
            return quickSort(subLeft) + [pivot] + quickSort(subRight)
        
print(quickSort([99,43,56,21,19,77]))
print(quickSort([1,4,1,2,9,5,2]))
