# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:34:49 2021

@author: 007ki
"""

n=int(input())
S=input()
s=S.split()
taxi=0
count3=0
count2=0
count1=0
for i in range(n):
    if s[i]=='4':
        taxi=taxi+1
    if s[i]=='3':
        count3=count3+1 
    if s[i]=='2':
        count2=count2+1
    if s[i]=='1':
        count1=count1+1
diff31=count3-count1
if count3!=0:
    if diff31==0:
        taxi=taxi+count3
        count1=0
    elif diff31>0:
        taxi=taxi+count3
        count1=0
    else:
        taxi=taxi+count3 
        count1=count1-count3
if count2!=0:
    if count2%2==0:
        taxi=taxi+(count2/2)
    else :
        r2=count2%2
        taxi=taxi+int(count2/2)
        diffr21=r2*2-count1
        if diffr21==0:
            taxi=taxi+r2
            count1=0
        elif diffr21>0:
            taxi=taxi+r2
            count1=0
        else:
            taxi=taxi+r2
            count1=count1-(r2*2) 
if count1!=0:
    if count1%4==0:
        taxi=taxi+count1/4
    elif count1<4:
        taxi=taxi+1
    elif count1>4 and count1%4!=0:
        taxi=taxi+int(count1/4)+(count1%4)
print(int(taxi))
    
        
    
        
    