# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:48:32 2021

@author: raj patil
"""
for i in range(int(input())):
    n = input()
    if n == n[::-1]:
        print('wins')
    else:
        print('loses')
    