# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:16:10 2021

@author: 007ki
"""

a=input()
a=list(a)
a[0]=a[0].upper()
ans=''
for i in range(len(a)):
    ans=ans+a[i]
print(ans)
