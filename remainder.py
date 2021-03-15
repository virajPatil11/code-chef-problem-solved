# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:12:22 2021

@author: raj patil
"""

def calculate_sum(A,B):
    N = A % B
    return N
t = int(input())

for i in range(t):
    A,B = map(int,input().split())

    print(calculate_sum(A,B))