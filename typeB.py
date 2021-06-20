# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:09:16 2021

@author: 007ki
"""

# n=int(input())
# a=input()
# A=a.split()
# b=[]
# for i in range(n):
#     b.append(int(A[i]))
# max1=b[0]
# for j in range(n):
#     if max1<b[j]:
#         max1=b[j]
# print(max1)
def prime(N):
    if N==1: return False
    if N==2: return True
    for k in range(3,int(N**0.5)+1,2):
        if(N%k==0): return False
    return True 
prime(7)


            
    
        
        
            

   