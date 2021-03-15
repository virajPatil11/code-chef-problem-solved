# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:12:56 2021

@author: raj patil
"""

t = int(input())
for i in range(t):
    num = int(input())

# To take input from the user
#num = int(input("Enter a number: "))

    factorial = 1

# check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print(factorial)