# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:08:06 2021

@author: raj patil
"""

# cook your dish here
x,y = input().split()
x = int(x)
y = float(y)

if(x%5==0 and x+0.50<=y):
    z = y-x-0.50
    print('%0.2f' %z)
else:
    z = y
    print('%0.2f'%z)