# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:08:16 2021

@author: 007ki
"""

a=input()
A=a.split()
v1=int(A[0])
v2=int(A[1])
v3=int(A[2])
even=v1+v2+v3
z=(v1-v2+v3)/2
y=(v2-v1+v3)/2
x=(v1-v3+v2)/2
if (even%2!=0) or (x<0 and y<0 and z<0):
    print("Impossible")
# elif True:
#     # if x<0 and y<0 and z<0:
#     #     print("Impossible")
#     # if type(x)!=int and type(y)!=int and  type(y)!=int:
#     #     print("Impossible")        
else:
    ans=str(x)+" "+str(y)+" "+str(z)
    print(ans)
    
       