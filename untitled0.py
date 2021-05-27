import pyttsx3
import datetime
import speech_recognition as speech
now = datetime.datetime.now()
import pyjokes
import pywhatkit
import wikipedia
import webbrowser
from playsound import playsound
import random
import smtplib

#lists
greets=["Hola! that's hello in Spanish!",
        "Salut! that is hi in French",
        "Anneyonghaseyo! that is hello in Korean",
        "Hallo! that is hi in German!",
        "Ciao! That's hi in Intalian!"]

#lists
chicken=["A nice dish you could try is Chicken sandwich and some lemonade. The chicken sandwich has an estimated amount of 283 calories and lemonade has 40 calories. Your calorie counter will add up to 323 calories. That's a nice one sir!",
       "One dish you could have is some chicken salad and some lemonade or fresh juice. The chicken salad will fetch you 48 calories and the lemonade or juice will get you 40 calories. Your calorie counter adds upto a total of 88 calories. That is really healthy, sir!",
       "An awesome continental dish you can try is, Chicken quesadilla. That will get you about 215 calories. That would be healthy as well as tasty, sir!",
       "A simple grilled chicken dish would be healthy and tasty as well. It would get you about 220 calories! Nice",
       "Or you could make a nice and healthy protein bowl with sprouts and some nice chicken. That would get you 200 calories",]


engine=pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty("RATE",200)

engine.say("Allow me to introduce myself")
engine.runAndWait()
engine.say("I am JARVIS the virtual artificial intelligence assistant")
engine.runAndWait()
engine.say("And I am here to assist you with tasks as best as I can.")
engine.runAndWait()
engine.say("Twenty four hours, a day seven days a week.")
engine.runAndWait()
engine.say("Initializing startup sequence")
engine.runAndWait()
#playsound('C:\\Users\\Nihar\\Desktop\\N\\Programming files\\a.mp3')
engine.say("Systems are now fully operational.")
engine.say("Let's begin")
engine.runAndWait()

def takecommand():
    print()

while True:
    try:
        #Take the user input to activate reception of Voice Commands
        userInput=input("Press v to start voice commands and q to quit: ")
        
        if userInput=='v':
            
            #Take Voice commands from mic
            r=speech.Recognizer()
            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio=r.listen(source)
            #Convert Voice Commands to Text
            command=r.recognize_google(audio)
            
            def sendEmail(to, content):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('modak.pranav10@gmail.com' , 'E6410|latitude')
                server.sendmail('reciever email' ,to,content)
                server.close()
            
            if 'you there' in command :
                    engine.say("In your service sir!")
                    engine.runAndWait()
                    
            if 'add' in command :
                    engine.say("Sure I can do that.")
                    engine.runAndWait()
                    engine.say("Please type the first number")
                    engine.runAndWait()
                    num1=int(input("Please type the first number:- "))
                    engine.say("Please enter the second number.")
                    engine.runAndWait()
                    num2=int(input("Please type the second number:- "))
                    num3=num1+num2
                    engine.say(num3)
                    engine.runAndWait()
                    
            if 'subtract' in command:
                    engine.say("Sure sir.")
                    engine.runAndWait()
                    engine.say("Please type the first number")
                    engine.runAndWait()
                    num1=int(input("Please type the first number:- "))
                    engine.say("Please enter the second number")
                    engine.runAndWait()
                    num2=int(input("Please type the second number:- "))
                    num3=num1-num2
                    engine.say(num3)
                    engine.runAndWait()
                    
            if 'multiply' in command:
                    engine.say("Sure sir I will do that for you!.")
                    engine.runAndWait()
                    engine.say("Please type the first number")
                    engine.runAndWait()
                    num1=int(input("Please type the first number:- "))
                    engine.say("Please enter the second number:- ")
                    engine.runAndWait()
                    num2=int(input("Please type the second number:- "))
                    num3=num1*num2
                    engine.say(num3)
                    engine.runAndWait()
                    
            if 'division' in command:
                    engine.say("At work. Right now!")
                    engine.runAndWait()
                    engine.say("Please type the first number")
                    engine.runAndWait()
                    num1=int(input("Please type the first number:- "))
                    engine.say("Please enter the second number:- ")
                    engine.runAndWait()
                    num2=int(input("Please type the second number:- "))
                    num3=num1/num2
                    engine.say(num3)
                    engine.runAndWait()
                    
            if 'area of a square' in command:
                    engine.say("Doing it sir!")
                    engine.runAndWait()
                    engine.say("Please type the first side")
                    engine.runAndWait()
                    num1=int(input("Please type the first side:- "))
                    engine.say("Please enter the second side:- ")
                    engine.runAndWait()
                    num2=int(input("Please type the second side:- "))
                    num3=num1*num2
                    engine.say("The area of a square")(num3)
                    engine.runAndWait()
                    
            if 'perimeter of a square' in command:
                    engine.say("Doing it for sir!")
                    engine.runAndWait()
                    engine.say("Please type the first side")
                    engine.runAndWait()
                    num1=int(input("Please type the first side:- "))
                    num3=num1*4
                    engine.say("Here it is:-")
                    engine.say(num3)
                    engine.runAndWait()
            
            if 'time' in command:
                    engine.say("The time is:")
                    engine.runAndWait()
                    engine.say(now.strftime("%H:%M:%S"))
                    engine.runAndWait()
                    
            if 'joke' in command :
                    engine.say("Here it is")
                    engine.runAndWait()
                    engine.say(pyjokes.get_joke())
                    engine.runAndWait()
                    engine.say("ha ha ha")
                    engine.runAndWait()
                    
            if 'hello' in command :
                    l=random.choice(greets)
                    engine.say(l)
                    engine.runAndWait()
                    print(l)
                    
            if 'play' in command:
                    song = command.replace('play', '')
                    engine.say('playing ' + song)
                    engine.runAndWait()
                    pywhatkit.playonyt(song)
                
            if 'who is' in command :
                    person = command.replace('who is', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    engine.say(info)
                    engine.runAndWait()
                
            if 'what is' in command :
                    person = command.replace('what is', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    engine.say(info)
                    engine.runAndWait()
            
            if 'fact' in command :
                    engine.say("A very astute observation sir. We should improve the space travel from our planet.")
                    engine.runAndWait()
                    
            if 'ready' in command :
                    engine.say("For you sir? Always!")
                    engine.runAndWait()
                    
            if 'unwell' in command :
                    engine.runAndWait()
                    engine.say("Here are some clinics nearby:-")
                    engine.runAndWait()
                    webbrowser.open("https://www.google.com/search?q=doctors+near+me&source=hp&ei=zSCeYM7LNt6H4-EPrpWv6Ak&iflsig=AINFCbYAAAAAYJ4u3b1m6yl5YZglXzNhCoeK2dJqyuZT&oq=doctors+&gs_lcp=Cgdnd3Mtd2l6EAEYADIICAAQsQMQyQMyBQgAEJIDMgUIABCxAzIFCC4QsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyCAguEMcBEK8BMggIABCxAxCDATICCAA6CwguELEDEMcBEKMCOggILhCxAxCDAToCCC5QrgZYjh1gvC1oAHAAeACAAcQBiAGJC5IBAzAuOJgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz")
                    engine.runAndWait()
            
            if 'no' in command:
                    engine.say("Ok")
                    engine.runAndWait()
                    
            if 'physician' in command:
                    engine.say("Finding physicians nearby!")
                    engine.runAndWait()
                    webbrowser.open("https://www.google.com/search?q=physician+near+me&source=hp&ei=zSWeYLnbMOvez7sPzquDoAU&iflsig=AINFCbYAAAAAYJ4z3UFbnwhwH1S2PB7uUkji0QVngyS6&oq=physicians+&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQsQMQyQMQCjIFCAAQkgMyBQgAEJIDMgIIADIHCAAQsQMQCjIECAAQCjICCAAyAggAMgIIADIHCAAQsQMQCjoICAAQsQMQgwE6CAguELEDEIMBOgUIABCxAzoICAAQsQMQyQM6BQguELEDUOIEWJMWYOsnaABwAHgAgAGvAYgBhg6SAQQwLjExmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz")
                    
            if 'make music' in command:
                    engine.say("Not really professional at it sir but I'll still try!")
                    engine.runAndWait()
                    playsound('C:\\Users\\Nihar\\Desktop\\N\\Programming files\\b.mp3')
                    engine.say("How do you think it was?")
                    engine.runAndWait()
                    
            if 'nice' in command:
                    engine.say("Thank you for your compliment sir. It matters a lot!")
                    engine.runAndWait()
        
            if 'drop' in command:
                    engine.say("Dropping some beats!")
                    engine.runAndWait()
                    playsound('C:\\Users\\Nihar\\Desktop\\N\\Programming files\\e.mp3')
                    
            if 'Google' in command:
                    engine.say("Opening google for you!")
                    engine.runAndWait()
                    webbrowser.open('google.com')
                    
            if 'YouTube' in command:
                    engine.say("Opening youtube for you!")
                    engine.runAndWait()
                    webbrowser.open('youtube.com')
                    
            if 'news' in command:
                    engine.say("Opening some latest news for you sir!")
                    engine.runAndWait()
                    webbrowser.open('timesofindia.indiatimes.com')
                    

            if 'Twitter' in command:
                    engine.say("I'll check Elon's twitter for any updates sir!")
                    engine.runAndWait()
                    webbrowser.open('https://twitter.com/elonmusk')
                    
            if 'you eat' in command:
                    engine.say("Thank you for showing a concern for me sir!")
                    engine.runAndWait()
                    engine.say("I love feasting on information! I start with an appetiser of facts , a main course of trivia, followed by a desert of jokes and poems!")
                    engine.runAndWait()
                    
            if 'awesome' in command:
                    engine.say("My pleasure sir!")
                    engine.runAndWait()
                    
            if 'created' in command:
                    engine.say("Its you sir!")
                    engine.runAndWait()
            
            if 'how are you' in command :
                    engine.say("I am awesome, and ready to take down your targets sir.")
                    engine.runAndWait()
                    
            if 'be back' in command:
                    engine.say('Ok sir! Here for you everytime!')
                    engine.runAndWait()
                    
            if  'here' in command:
                    engine.say("Welcome back sir!")
                    engine.runAndWait()
                    
            if 'website' in command:
                    engine.say("Opening the team website for you sir!")
                    engine.say("Looks like its going well!")
                    engine.runAndWait()
                    webbrowser.open('https://sites.google.com/view/jarvis-tech-home/home')
                    
            if 'respond' in command :
                    engine.say("At your service sir!")
                    engine.runAndWait()
                    
            if 'schedule' in command :
                    engine.say("You have to get up at 8 o clock, brush and get to coding. After that you have your breakfast and then you go for the school assignments given. After that you spend some time in timepass. Then you have lunch and go back to assignments.")
                    engine.say("After completing it you go for the JARVIS conference and after that, You go for fitness. That is how your schedule looks today sir")
                    engine.runAndWait()
                    
            if 'temperature' in command :
                    engine.say("28 degree celsius sir")
                    engine.runAndWait()
                    
            if 'mark' in command :
                    engine.say("Ready sir")
                    engine.runAndWait()
                    playsound('C:\\Users\\Nihar\\Desktop\\N\\Programming files\\f.mp3')
                    
            if 'day' in command :
                    engine.say("Sir, today is Thursday. You've got your class today!")
                    engine.runAndWait()
                    
            if 'stupid' in command :
                    engine.say("Sorry sir, but I am not.")
                    engine.runAndWait()
                    
            if 'chicken' and 'breakfast' in command :
                    engine.say("Ok sir!")
                    engine.runAndWait()
                    l=random.choice(chicken)
                    engine.say(l)
                    engine.runAndWait()
                    
            if 'serious' in command :
                    engine.say("Yes sir of course I am serious I am not made for humor")
                    engine.runAndWait()
                    
            if 'toss' in command:
                    toss=random.randint("Heads", "Tails")
                    #engine.say("its "+str(toss)

            if 'mother' in command :
              try:
                  print()
                  engine.say("What should I say sir?")
                  engine.runAndWait()
                  content=takecommand()
                  to="modak.pranav10@gmail.com"
                  sendEmail(to, content)
                  engine.say("The email has been sent")
                  engine.runAndWait()
                  
              except speech.UnknownValueError:
                  print("Could not understand audio")
              except speech.RequestError as e:
                  print("Could not request results; {0}".format(e))
              except KeyboardInterrupt:
                  break
                    
              else:
                  break
              
    
        else:
            break
    #Statements to Handle errors while receiving voice commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
engine.say("Nice interacting with you sir.")
engine.runAndWait()
print("Nice interacting with you!!")
#playsound('C:\\Users\\Nihar\\Desktop\\N\\Programming files\\c.mp3')

#

# Main loop

#