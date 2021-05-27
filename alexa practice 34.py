# -*- coding: utf-8 -*-
"""
Created on Sat May  8 14:22:05 2021

@author: modak_ng8awn0
"""


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
                print("Speak first number:")
                audio = AudioIn.listen(source)
    
            command=AudioIn.recognize_google(audio)
            print("You said " + command )
            engine.say("YOU SAID "+command)
            engine.runAndWait()
            
            with Inexa.Microphone() as source:
                AudioIn.adjust_for_ambient_noise(source)
                print("Speak second number:")
                audio = AudioIn.listen(source)
    
            dammand=AudioIn.recognize_google(audio)
            print("You said " + dammand )
            engine.say("YOU SAID "+dammand)
            engine.runAndWait()
            
            with Inexa.Microphone() as source:
                AudioIn.adjust_for_ambient_noise(source)
                print("speak addition subtraction multiplication or division:")
                audio = AudioIn.listen(source)
    
            sommand=AudioIn.recognize_google(audio)
            print("You said " + sommand )
            engine.say("YOU SAID "+sommand)
            engine.runAndWait()
            if sommand == "addition":
                print("the addition is: "+str(dammand+command))
                engine.say("the addition is: "+str(dammand+command))
                engine.runAndWait()
                
            elif sommand == "subtraction":
                print("the subtraction is: "+str(command-dammand))
                engine.say("the subtraction is: "+str(command-dammand))
                engine.runAndWait()
            
            elif sommand == "multiplication":
                print("the multiplication is: "+str(command*dammand))
                engine.say("the multiplication is: "+str(command*dammand))
                engine.runAndWait()
            
            elif sommand == "division":
                print("the divsion is: "+str(command/dammand))
                engine.say("the division is: "+str(command/dammand))
                engine.runAndWait()
        else:
            print("Module not found")
            engine.say("Module not found")
            engine.runAndWait()
            break
    except Inexa.UnknownValueError:
        print("Could not understand audio")
    except Inexa.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break


    
print("bye")