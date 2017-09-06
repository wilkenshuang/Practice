#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/6 15:23
# @Author  : Wilkenshuang
# @File    : test2.py
# @Software: PyCharm Community Edition

def biggestFactor(a,b):
    r0=max(a,b)
    r1=min(a,b)
    r2=r0 % r1
    if r2==0:
        return r1
    else:
        a,b=r1,r2
        return biggestFactor(a,b)
print(biggestFactor(1680,640))
