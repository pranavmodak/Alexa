# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:34:40 2021

@author: modak_ng8awn0
"""


import pyttsx3
engine=pyttsx3.init()
engine.setProperty("RATE", 200)

a= input("enter your name: ")
engine.say("hello" +a+"how arre you today?" )

engine.runAndWait()