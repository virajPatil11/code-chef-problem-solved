# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 17:29:34 2021

@author: raj patil
"""

for i in range(int(input())):
    A,B = map(int,input().split())
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")
    