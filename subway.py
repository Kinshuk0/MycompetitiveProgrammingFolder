# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:51:58 2021

@author: 007ki
"""

b=input()
A=b.split()
n=int(A[0])
m=int(A[1])
a=int(A[2])
b=int(A[3])
remainder=n%m
if n>=m:
    if remainder==0:
        ans=int((n/m))*b
        ans1=n*a
    else:
        ans=int((n/m))*b + remainder*a
        ans1=n*a
    print(min(ans,ans1))
else:
    ans=n*a
    ans1=m*b
    print(min(ans,ans1))
   