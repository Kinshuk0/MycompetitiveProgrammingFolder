# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:55:29 2021

@author: 007ki
"""

n=int(input())
s=input()
a=s.split()
A=[]
for i in range(n):
    A.append(int(a[i]))
even=0
odd=0
e=[]
o=[]
for i in range(n):
    if A[i]%2==0:
        even=even+1
        e.append(i+1)
    else:
        odd=odd+1
        o.append(i+1)
if even==1:
    print(e[0])
else:
    print(o[0])
    
        
        
        
    
    
    
