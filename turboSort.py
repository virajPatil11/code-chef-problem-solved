# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:43:51 2021

@author: raj patil
"""

t = int(input())
numbers = []
for i in range(t):
    num = int(input())
    numbers.append(num)
    
numbers.sort()
for i in range(t):
    print(numbers[i])