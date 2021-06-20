# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:49:11 2021

@author: 007ki
"""

s=input()
n=len(s)
S=[]
A=[]
count=n
for i in range(n):
    S.append(s[i])
for j in range(n):
    for k in range(j+1,n):
        if S[j]==S[k]:
            count=count-1
if count%2!=0:
    print("IGNORE HIM!")    
else:
    print("CHAT WITH HER!")
            
