# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:02:43 2021

@author: raj patil
"""
for _ in range(int(input())):
    d,n = map(int, input().split())
    for i in range(d):
        n = (n*(n+1)//2)
    print(n)    