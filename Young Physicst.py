# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:28:28 2021

@author: 007ki
"""

n=int(input())
a=[]
x=[]
y=[]
z=[]
for k in range(n):
    a.append(input())
for i in range(n):
    x.append(int((a[i].split())[0]))
    y.append(int((a[i].split())[1]))
    z.append(int((a[i].split())[2]))
def sumarray(a):
    sumarray=0
    for j in range(len(a)):
        sumarray=sumarray+a[j]
    return sumarray
xsum=sumarray(x)
ysum=sumarray(y)
zsum=sumarray(z)
if xsum==0 and ysum==0 and zsum==0 :
    print('YES')
else:
    print('NO')
    


    