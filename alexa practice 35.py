# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:16:48 2021

@author: modak_ng8awn0
"""


addcity=[]
import speech_recognition as Inexa
import pyttsx3

engine=pyttsx3.init()
engine.setProperty("RATE", 200)

while True:
    
    try:
        print ('Press v & Speak:')
        read= input()
        if read=='v':
            AudioIn = Inexa.Recognizer()
            
            with Inexa.Microphone() as source:
                AudioIn.adjust_for_ambient_noise(source)
                print("enter name of city:")
                audio = AudioIn.listen(source)
    
            command=AudioIn.recognize_google(audio)
            print("You said " + command )
            engine.say("YOU SAID "+command)
            engine.runAndWait() 
            addcity.append(command)
            playmore=input("do you want to continue?y/n: ").lower
            if playmore=="y":
                print("printing")
            else:
                break
                
        else:
            break
            
    
   
    except Inexa.UnknownValueError:
        print("Could not understand audio")
    except Inexa.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    
print(addcity)
engine.say(addcity)
engine.runAndWait()   
print("bye")