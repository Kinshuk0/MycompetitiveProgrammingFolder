# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:41:15 2021

@author: 007ki
"""
n=int(input())
b=input()
B=b.split()
C=[]
finalcheck=[]
primearray=[]
for i in range(n):
    C.append(int(B[i]))
max1=0
for k in range(n):
    if C[k]>max1:
        max1=C[k]

for j in range(2,int(max1**0.5)+1):
    flag=0
    for l in range(2,j):
        if(j % l==0):
            flag = 1
            break
    
    if(flag==0):
        primearray.append(float(j))
for x in range(n):
    
        finalcheck.append(C[x]**0.5)
for r in range(len(finalcheck)):
    if finalcheck[r] in primearray:
        print('YES')
    else:
        print('NO')

    
    
    
        
    
    
    
    
    
    