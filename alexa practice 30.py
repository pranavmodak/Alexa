# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:54:46 2021

@author: modak_ng8awn0
"""


a={"pranav,latitude"
   "alex, pad",
   "tia, E6410"}
for x in range(3):
    username=input("enter your username: ").lower()
    userpass=input("enter your password: ").lower()

    if username=="pranav":
        if userpass=="latitude":
            print("correct password")
            break
        else:
            print("wrong password")
    if username=="alex":
        if userpass=="pad":
            print("correct password")
            break
        else:
            print("wrong password")
    if username=="tia":
        if userpass=="e6410":
            print("correct password")
            break
        else:
            print("wrong password")
            
        