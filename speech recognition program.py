import speech_recognition as speech
import pyttsx3

engine=pyttsx3.init()
engine.setProperty("RATE", 200)

while True:
    try:
        print ('Press v & Speak:')
        read= input()
        if read=='v':
            AudioIn = speech.Recognizer()
            
            with speech.Microphone() as source:
                AudioIn.adjust_for_ambient_noise(source)
                print("Speak:")
                audio = AudioIn.listen(source)
    
            command=AudioIn.recognize_google(audio)
            print("You said " + command )
            engine.say("YOU SAID "+command)
            engine.runAndWait() 
        else:
            break
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break    
    
print("bye")