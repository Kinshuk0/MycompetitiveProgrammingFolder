# -*- coding: utf-8 -*-
"""
Created on Sat May 22 03:00:02 2021

@author: 007ki
"""

s=input()
m=int(input())
q=[]
for j in range(m):
    q.append(input())
for i in range(m):
    ans=0
    Q=q[i].split()
    l=int(Q[0])
    r=int(Q[1])
    for k in range(l,r):
        if s[k-1]==s[k]:
            ans=ans+1
    print(ans)    
    
    