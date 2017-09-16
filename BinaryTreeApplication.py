#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 10:34
# @Author  : Wilkenshuang
# @File    : test3.py
# @Software: PyCharm Community Edition

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def preTraverse(root):
    if root==None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)
def midTraverse(root):
    if root==None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)
def afterTraverse(root):
    if root==None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)

def findTree(preList,midList,afterList):
    if len(preList)==0:
        return
    if len(preList)==1:
        afterList.append(preList[0])
        return
    root=preList[0]
    n=midList.index(root)

if __name__=='__main__':
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print('前序遍历：')
    preTraverse(root)
    print('\n')
    print('中序遍历：')
    midTraverse(root)
    print('\n')
    print('后序遍历')
    afterTraverse(root)
    print('\n')

def findTree(preList,midList,afterList):
    if len(preList)==0:
        return
    if len(preList)==1:
        afterList.append(preList[0])
        return
    root=preList[0]
    n=midList.index(root)
    findTree(preList[1:n+1],midList[:n],afterList)
    findTree(preList[n+1:],midList[n+1:],afterList)
    afterList.append(root)

preList=list('DBACEGF')
midList=list('ABCDEFG')
afterList=[]
findTree(preList,midList,afterList)
print(afterList)
