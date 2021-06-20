# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:55:02 2021

@author: 007ki
"""

n=int(input())
A=[]
x=0
for i in range(n):
    A.append(input())
for j in range(n):
    if A[j][0]=='-':
        x=x-1
    elif A[j][1]=='-':
        x=x-1
    else:
        x=x+1
print(x)

