# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:37:43 2021

@author: 007ki
"""

a=input()
b=a.split()
n=int(b[0])
k=int(b[1])
c=input()
d=c.split()
height=[]
for l in range(len(d)):
    height.append(int(d[l]))
minm=0
ans=1
for j in range(k):    
    minm=minm+height[j]
for i in range(n-k):
    curr=minm-height[i]+height[i+k]
    if minm>curr:
        minm=curr
        ans=i+2       
print(ans)

        