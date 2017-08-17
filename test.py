# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:21:26 2017

@author: wilkenshuang

假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码
按字典序排序，形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba,
baa, baaa, baab, baac … …, yyyw, yyyx, yyyy 其中a的Index为0，aa的Index
为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码
对应的Index.

腾讯校招题，考点：组合
"""

import sys

input=sys.stdin.readline().strip()
v1=25**3+25**2+25**1+1
v2=25**2+25**1+1
v3=25**1+1
v4=1
v=[v1,v2,v3,v4]
output,i=len(input)-1,0
while i<len(input):
    output+=(ord(input[i])-ord('a'))*v[i]
    i+=1
print(output)