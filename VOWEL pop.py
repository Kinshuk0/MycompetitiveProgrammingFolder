# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:12:36 2021

@author: 007ki
"""

S=input()
s=S.lower()
ans=""
for i in s:
    if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!="y":
        ans=ans+"."+i
print(ans)
        