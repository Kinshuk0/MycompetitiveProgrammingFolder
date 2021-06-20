# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:29:33 2021

@author: 007ki
"""

n=int(input())
s=input()
S=[]
count=0
for i in range(n):
    S.append(s[i])
for j in range(n-1):
    if S[j]==S[j+1]:
        count=count+1
print(count)
