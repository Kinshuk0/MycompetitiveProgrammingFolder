# -*- coding: utf-8 -*-
"""
Created on Sat May 22 03:54:13 2021

@author: 007ki
"""

s=input()
m=int(input())
q=[]
sample=[]
presum=[]
for j in range(m):
    q.append(input())
for l in range(len(s)-1):
    if s[l]==s[l+1]:
        sample.append(1)
    else:
        sample.append(0)
presum.append(sample[0])
for k in range(1,len(sample)):    
    presum.append(presum[k-1]+sample[k])
print(presum,sample)
for i in range(m):
    Q=q[i].split()
    l=int(Q[0])
    r=int(Q[1])
    ans=presum[r-2]-presum[l-1]
    print(ans)