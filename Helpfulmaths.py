# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 19:49:28 2021

@author: 007ki
"""

a=input()
b=[]
k=0
while k<len(a):
    b.append(int(a[k]))
    k=k+2
for i in range(0, len(b)):    
    for j in range(i+1, len(b)):    
        if(b[i] > b[j]):    
            temp = b[i];    
            b[i] = b[j];    
            b[j] = temp;
op=''
for l in range(len(b)):
    if l<(len(b)-1):
        op=op+str(b[l])+'+'
    else:
        op=op+str(b[l])
print(op)
    
    
    
    
    