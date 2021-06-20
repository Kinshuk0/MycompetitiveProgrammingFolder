# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:39:06 2021

@author: 007ki
"""

n=int(input())
if n==1:
    print("Happy Alex")
else:
    pq=[]
    price=[]
    quality=[]
    for i in range(n):
        pq.append(input())
    for j in range(n):
        a=pq[j].split()
        price.append(int(a[0]))
        quality.append(int(a[1]))
    maxprice=0
    pi=0
    maxqua=0
    qi=0
    for k in range(n):
        if price[k]>maxprice:
            maxprice=price[k]
            pi=k
        if quality[k]>maxqua:
            maxqua=quality[k]
            qi=k
    if maxprice==maxqua:
        print("Happy Alex")
    else:
        if qi==pi:
            print("Poor Alex") 
        else:
            print("Happy Alex")
        
    
    
    
