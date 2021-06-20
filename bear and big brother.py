# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:23:53 2021

@author: 007ki
"""

n=input()
k=n.split()
a=int(k[0])
b=int(k[1])
years=0
if a==b:
    print(1)
else:
    
  while b>a:
      a=a*3
      b=b*2
      years=years+1
  if a==b:
     print(years+1)
  else:
      print(years)

    