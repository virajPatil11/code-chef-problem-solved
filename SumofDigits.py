# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:10:48 2021

@author: raj patil
"""
#defining a function
def calculate_sum(N):
    sum = 0
    #checking if input is more than 0 or not
    while(N!=0):
        sum += N%10
        N = N//10
    return sum    
t = int(input())

for i in range(t):
    N = int(input())
    #calling function
    print(calculate_sum(N))