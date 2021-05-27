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
import tkinter
import tkinter.messagebox
import pickle
import time

score2=0 

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
                    
            if 'respond' in command :
                    engine.say("At your service sir!")
                    engine.runAndWait()
                    
            if 'schedule' in command :
                    engine.say("You have to get up at 8 o clock, brush and get to coding. After that you have your breakfast and then you go for the school assignments given. After that you spend some time in timepass. Then you have lunch and go back to assignments.")
                    engine.say("After completing it you go for the JARVIS conference and after that, You go for fitness. That is how your schedule looks today sir")
                    engine.runAndWait()
                    
            if 'temperature' in command :
                    engine.say("30 degree celsius sir")
                    engine.runAndWait()
                    
            if 'mark' in command :
                    engine.say("Ready sir")
                    engine.runAndWait()
                    playsound('C:\\Users\\Nihar\\Desktop\\N\\Programming files\\f.mp3')
                    
            if 'stupid' in command :
                    engine.say("Sorry sir, but I am not.")
                    engine.runAndWait()
                    
            if 'chicken' and 'breakfast' in command :
                    engine.say("Ok sir!")
                    engine.runAndWait()
                    l=random.choice(chicken)
                    engine.say(l)
                    engine.runAndWait()
                    
            if 'Gmail' in command :
                    engine.say("Yes sir I'll do it for you!")
                    engine.runAndWait()
                    webbrowser.open('gmail.com')
                    
            if 'serious' in command :
                    engine.say("Yes sir I am not made for humour.")
                    engine.runAndWait()
                    
            if 'task list' in command :
                    engine.say("Opening task list")
                    engine.runAndWait()
                    root = tkinter.Tk()
                    root.title("Your To do List. ")
                    
                    def add_task():
                        task = entry_task.get()
                        if task != "":
                            listbox_tasks.insert(tkinter.END, task)
                            entry_task.delete(0, tkinter.END)
                        else:
                            tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")
                    
                    def delete_task():
                        try:
                            task_index = listbox_tasks.curselection()[0]
                            listbox_tasks.delete(task_index)
                        except:
                            tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
                    
                    def load_tasks():
                        try:
                            tasks = pickle.load(open("tasks.dat", "rb"))
                            listbox_tasks.delete(0, tkinter.END)
                            for task in tasks:
                                listbox_tasks.insert(tkinter.END, task)
                        except:
                            tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")
                    
                    def save_tasks():
                        tasks = listbox_tasks.get(0, listbox_tasks.size())
                        pickle.dump(tasks, open("tasks.dat", "wb"))
                    
                    # Create GUI
                    frame_tasks = tkinter.Frame(root)
                    frame_tasks.pack()
                    
                    listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
                    listbox_tasks.pack(side=tkinter.LEFT)
                    
                    scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
                    scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
                    
                    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
                    scrollbar_tasks.config(command=listbox_tasks.yview)
                    
                    entry_task = tkinter.Entry(root, width=50)
                    entry_task.pack()
                    
                    button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
                    button_add_task.pack()
                    
                    button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
                    button_delete_task.pack()
                    
                    button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
                    button_load_tasks.pack()
                    
                    button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
                    button_save_tasks.pack()
                    
                    root.mainloop()
                    if 'quiz' in command:

                        engine.say("Take this tech-trivia to sharpen your mind.")
                        engine.runAndWait()
                        time.sleep(1)
                        
                        print("Question 1")      
                        engine.say("Question 1")
                        engine.runAndWait()
                        print("Who is the C.E.O of spacex and Tesla motors?")
                        engine.say()
                        engine.runAndWait()
                        print("A.Elon Musk: B.Jeff Bezos: C.Larry Elison D.Lyndon Rive")
                        engine.say("A.Elon Musk: B.Jeff Bezos: C.Larry Elison D.Lyndon Rive")
                        engine.runAndWait()
                        takecommand()
                    if 'elon musk' or 'option a' in command :
                            engine.say("That's intelligent! Right answer!")
                            engine.runAndWait()
                            score2=score2+1
                    else:
                            engine.say("Nope! that is the wrong answer!")
                            engine.runAndWait()
                            engine.say("It was Elon musk")
                            engine.runAndWait()
                            score2=score2+0
                        # question 1 over
                            
                            print("Question 2")  
                            engine.say("Question 2")
                            engine.runAndWait()    
                            print("Which of the following is a crypto currency?")
                            engine.say("Which of the following is a crypto currency?")
                            engine.runAndWait()
                            print("A Bitcoin B Dogecoin C. Litecoin D. All of them")
                            engine.say("A Bitcoin B Dogecoin C. Litecoin D. All of them")
                            engine.runAndWait()
                            takecommand()
                            if 'd' or 'option d' in command :
                                engine.say("That is the right answer!")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("Nope that is the wrong answer!")
                                engine.runAndWait()
                                engine.say("The correct answer was, All of them")
                                engine.runAndWait()
                                score2=score2+0
                            # question 2 over
                                
                            print("Question 3")  
                            engine.say()
                            engine.runAndWait()    
                            print("Which of the following is not an A.I assistant of Tony Stark from MCU?")
                            engine.say("Which of the following is not an A.I assistant of Tony Stark from MCU?")
                            engine.runAndWait()
                            print("A. JARVIS B. EDITH C. FRIDAY D. VISION")
                            engine.say("A JARVIS B EDITH C FRIDAY D VISION")
                            engine.runAndWait()
                            takecommand()
                            if 'd' or 'option d' in command :
                                engine.say("That is the correct answer!")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("Oops! That's the wrong one!")
                                engine.runAndWait()
                                engine.say("The correct answer is D Vision")
                                score2=score2+0
                            # question 3 over
                                
                            print("Question 4")     
                            engine.say("Question 4")
                            engine.runAndWait() 
                            print("What was the serial number of the suit Tony Stark wore in Avenger's infinity war?")
                            engine.say("What was the serial number of the suit Tony Stark wore in Avenger's infinity war?")
                            engine.runAndWait()
                            print("A MARK 47, B MARK 50, C MARK 33 D MARK 35")
                            engine.say("A MARK 47, B MARK 50, C MARK 33 D MARK 35")
                            engine.runAndWait()
                            takecommand()
                            if 'b' or 'option b' in command :
                                engine.say("Wow that is indeed the right answer!")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("Oops that was a close one but sorry that is the wrong one")
                                engine.runAndWait()
                                engine.say("The correct answer is the MARK 50 armour")
                                engine.runAndWait()
                                score2=score2+0
                            # question 4 over
                                
                            print("Question 5")      
                            engine.say("Question 5")
                            engine.runAndWait()
                            print("Which lander was chosen by NASA to land on the moon?")
                            engine.say("Which lander was chosen by NASA to land on the moon?")
                            engine.runAndWait()
                            print("A. Dynetics B. Starship C. Human landing system D. SLS block")
                            engine.say("A. Dynetics B. Starship C. Human landing system D. SLS block")
                            engine.runAndWait()
                            takecommand()
                            if 'b' or 'option b':
                                engine.say("Awesome! that is the right one")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("Oh no. That is the wrong one.")
                                engine.runAndWait()
                                engine.say("The correct one is B. Starship")
                                engine.runAndWait()
                                score2=score2+0
                            # question 5 over
                                
                            print("Question 6") 
                            engine.say("Question 6")
                            engine.runAndWait()     
                            print("Who is explicitely known as the technoking?")
                            engine.say("Who is explicitely known as the technoking?")
                            engine.runAndWait()
                            print("A.Elon Musk B.Mark Zuckerberg C.Jeff Bezos D.Larry Elison")
                            engine.say("A.Elon Musk B.Mark Zuckerberg C.Jeff Bezos D.Larry Elison")
                            engine.runAndWait()
                            takecommand()
                            if 'a' or 'option a':
                                engine.say('Thats just perfect!')
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say('Nope you stumbled upon this question')
                                engine.runAndWait()
                                engine.say("The correct answer is Elon musk. ")
                                score2=score2+0
                            # question 6 over
                                
                            print("Question 7")  
                            engine.say()
                            engine.runAndWait()    
                            print("Where is a supercollider?")
                            engine.say("Where is a supercollider?")
                            engine.runAndWait()
                            print("A.Waxahachie, Texas, B.Cern, Switzerland C. Paris, France D. Toronto, Canada.")
                            engine.say("A.Waxahachie, Texas, B.Cern, Switzerland C. Paris, France D. Toronto, Canada.")
                            engine.runAndWait()
                            takecommand()
                            time.sleep(5)
                            if'b' or 'option b' in command :
                                engine.say("Yes, This the correct one!")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("Nope, wrong choice")
                                engine.runAndWait()
                                engine.say("The correct answer is Cern Switzerland")
                                score2=score2+0
                            # question 7 over
                                
                            print("Question8")    
                            engine.say("Question8")
                            engine.runAndWait()  
                            print("Which country leads in technological advancement?")
                            engine.say("Which country leads in technological advancement?")
                            engine.runAndWait()
                            print("A.England B.Japan C.USA D.Canada")
                            engine.say("A.England B.Japan C.USA D.Canada")
                            engine.runAndWait()
                            takecommand()
                            if 'b' or 'option b'in command :
                                engine.say("Awesome! That is the right one!")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("You almost got it right! But its the wrong one.")
                                engine.runAndWait()
                                engine.say("The correct answer is Japan.")
                                score2=score2+0
                            # question 8 over
                                
                            print("Question 9")      
                            engine.say("Question 9")
                            engine.runAndWait()
                            print("Which is a programming language?")
                            engine.say("Which is a programming language?")
                            engine.runAndWait()
                            print("A. Roff B. Python C. Ruby D. All of them")
                            engine.say("A. Roff B. Python C. Ruby D. All of them")
                            engine.runAndWait()
                            takecommand()
                            if 'd' or 'option d' in command:
                                engine.say("Wow! That is indeed the right answer")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("Oh so close but the wrong answer.")
                                engine.runAndWait()
                                engine.say("The correct answer is D. All of them")
                                engine.runAndWait()
                                score2=score2+0
                            # question 9 over
                                
                            print("Question 10") 
                            engine.say("Question 10")
                            engine.runAndWait()     
                            print("What is the name of Mark Zuckerberg's AI assistant?")
                            engine.say("What is the name of Mark Zuckerberg's AI assistant?")
                            engine.runAndWait()
                            print("A JARVIS B Cortana C Facebook M. D Blackberry")
                            engine.say("A JARVIS B Cortana C Facebook M. D Blackberry")
                            engine.runAndWait()
                            time.sleep(5)
                            if 'a' or 'option a' in command :
                                engine.say("You indeed know a lot")
                                engine.runAndWait()
                                score2=score2+1
                            else:
                                engine.say("That was actually a simple one!")
                                engine.runAndWait()
                                engine.say("The answer was A. JARVIS")
                                engine.runAndWait()
                                score2=score2-1
                            # question 10 over
                                
                            
                                
                            print("your score is"+str(score2))
                            if score2==10:
                                engine.say("What a sharp brain.")
                                engine.runAndWait()
                            elif score2>5:
                                engine.say("A litte study would help!")
                                engine.runAndWait()
                            elif score2<3:
                                engine.say("You need some practice!")
                                engine.runAndWait()

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