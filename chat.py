# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:03:36 2021

@author: 007ki
"""

s=input()
n=len(s)
flag=0
for i in range(n):
    if s[i] == 'h':
        for j in range(i+1,n):
            if s[j]=='e':
                for k in range(j+1,n):
                    if s[k]=='l':
                        for l in range(k+1,n):
                            if s[l]=='l':
                                for m in range(l+1,n):
                                    if s[m]=='o':
                                        flag=1
if flag==1:
    print('YES')
else:
    print('NO')                                        
                    
        
    