# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:15:36 2021

@author: raj patil
"""
for i in range(int(input())):
    n = input()
    x = n.count("a")
    y = n.count("b")
    if x > y :
        print(y)
    elif x < y :
        print(x)
    else:
        print(x)