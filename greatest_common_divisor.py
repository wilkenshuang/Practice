#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/6 15:23
# @Author  : Wilkenshuang
# @File    : test2.py
# @Software: PyCharm Community Edition

'''
寻找两个数的最大公因子，解法用到了欧几里得算法，即令r0= a，r1 = b，然后计算相继的商和余数，
直到rn+1为0，最后的非零余数rn就是a与b的最大公因子。
'''

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
