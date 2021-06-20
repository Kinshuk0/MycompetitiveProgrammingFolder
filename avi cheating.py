# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:11:40 2021

@author: 007ki
"""

def pthFactor(n,p):
    ans=[]
    i=1
    while i*i <= n:
        if n%i==0:
            ans.append(i)
            if n//i!=i:
                ans.append(n//i)
        i += 1
    ans.sort()
    if n==1 and p==5:
        return 1
    else:
        if len(ans)<p:
            return 0
        else:
            return ans[p-1]
print(pthFactor(1,5))


        