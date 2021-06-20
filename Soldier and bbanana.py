# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:04:38 2021

@author: 007ki
"""

a=input()
b=a.split()
k=int(b[0]) #cost of 1st banana
n=int(b[1]) #money he have 
w=int(b[2]) #no of banana he has to buy
totalsum=int(k*w*(w+1)*(0.5))
udhar=totalsum-n
if udhar>=0:
    print(udhar)
else:
    print(0)
