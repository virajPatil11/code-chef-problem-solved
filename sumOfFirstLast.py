# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:43:51 2021

@author: raj patil
"""

t = int(input())
for i in range(t):
    sum = 0
    num = input()
    sum = sum + int(num)%10 + int(num)//pow(10,len(num) - 1)
    print(sum)