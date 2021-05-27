# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:02:40 2021

@author: modak_ng8awn0
"""


import pyttsx3
engine=pyttsx3.init()
engine.setProperty("RATE", 200)
engine.say("hello")
engine.runAndWait()