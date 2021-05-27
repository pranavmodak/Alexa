import pyttsx3

engine=pyttsx3.init()
engine.setProperty("RATE", 300)

lista=["Akshay Kumar,Vidya Balan, Amitab Bachan, Tom Hanks, Thomas Jeffrey"]

a=input("Which one you like?: ")
engine.say("ok you like"+a)
engine.runAndWait()