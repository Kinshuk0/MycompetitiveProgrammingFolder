# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:39:10 2021

@author: 007ki
"""

n=int(input())
luckyno=[4,7,47,74,447,474,744,444,774,747,477,777]
flag=0
if n in luckyno:
    print('YES')
else:
    for i in range(len(luckyno)):
        if n%luckyno[i]==0:
            flag=1
            break
    if flag==1:
        print('YES')
    else:
        print('NO')
        
    