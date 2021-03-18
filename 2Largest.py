# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:16:05 2021

@author: raj patil
"""
    
T=int(input())

while(T):
    l=[int(i) for i in input().split()]
    l.sort()
    print(l[-2])
    T -= 1