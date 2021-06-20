# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:40:59 2021

@author: 007ki
"""

def maxpieces(n,a,b,c):
    if n==0: return 0
    if n<0:  return -1
    res=max(maxpieces(n-a,a,b,c),maxpieces(n-b,a,b,c),maxpieces(n-c,a,b,c))
    if res==-1: return -1
    return res + 1
a=input()
A=a.split()
print(maxpieces(int(A[0]),int(A[1]),int(A[2]),int(A[3])))
