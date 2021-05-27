import speech_recognition as Inexa
import pyttsx3

engine=pyttsx3.init()
engine.setProperty("RATE", 200)

while True:
    print("Hello, enter any sport name and i will give you info")
    print("the sport data availale are cricket, football, tennis, basketball and handball")   
    print ('Press v & Speak:')
    read= input()
    if read=='v':
        AudioIn = Inexa.Recognizer()
        
        with Inexa.Microphone() as source:
            AudioIn.adjust_for_ambient_noise(source)
            print("Speak:")
            audio = AudioIn.listen(source)

        command=AudioIn.recognize_google(audio)
        print("You said " + command )
        engine.say("YOU SAID "+command)
        engine.runAndWait() 
        
        if "cricket" in command:
            print("Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard pitch with a wicket at each end, each comprising two bails balanced on three stumps.")
            engine.say("Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard pitch with a wicket at each end, each comprising two bails balanced on three stumps.")
            engine.runAndWait()
        if "football" in command:
            print("Association football, more commonly known as simply football or soccer, is a team sport played by all genders with a spherical ball between two teams of 11 players. It is played by approximately 250 million players in over 200 countries and dependencies, making it the world's most popular sport.")
            engine.say("Association football, more commonly known as simply football or soccer, is a team sport played by all genders with a spherical ball between two teams of 11 players. It is played by approximately 250 million players in over 200 countries and dependencies, making it the world's most popular sport.")
            engine.runAndWait()
        if "basket ball" in command:
            print("Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball through the defender's hoop while preventing the opposing team from shooting through their own hoop.")
            engine.say("Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball through the defender's hoop while preventing the opposing team from shooting through their own hoop.")
            engine.runAndWait()            
        if "tennis" in command:
            print("Tennis is a racket sport that can be played individually against a single opponent or between two teams of two players each. Each player uses a tennis racket that is strung with cord to strike a hollow rubber ball covered with felt over or around a net and into the opponent's court.")
            engine.say("Tennis is a racket sport that can be played individually against a single opponent or between two teams of two players each. Each player uses a tennis racket that is strung with cord to strike a hollow rubber ball covered with felt over or around a net and into the opponent's court.")
            engine.runAndWait()            
        if "hand ball" in command:
            print("Handball is a team sport in which two teams of seven players each pass a ball using their hands with the aim of throwing it into the goal of the other team. A standard match consists of two periods of 30 minutes, and the team that scores more goals wins.")
            engine.say("Handball is a team sport in which two teams of seven players each pass a ball using their hands with the aim of throwing it into the goal of the other team. A standard match consists of two periods of 30 minutes, and the team that scores more goals wins.")
            engine.runAndWait() 
        else:
            print("the sport not in the list")
            engine.say("the sport not in the list")
            engine.runAndWait()
            break
        
    
    
print("bye")