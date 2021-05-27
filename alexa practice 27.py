# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:20:38 2021

@author: modak_ng8awn0
"""


while 1:
    a=int(input("enter a number: "))
    print("the square is "+ str(a*2))
    b=input("do you want to continue: ").lower()
    if b == "yes":
        print("ok")
    else:
        break