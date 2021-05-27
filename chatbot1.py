"""
chatbot on riddles and jokes

riddles
1. what you take to eat but dont eat? - plate
2. if a red house is made up of red bricks, blue house of blue then what is a green house made up of? - glass
3. what has foot on each side and one in the middle? - yardstick

jokes
1. why did the nurse need a red pen at work - in case she needed to draw blood

2.why was 6 afraid of 9 on new year eve - because 9,8,7

3.why couldnt pony sing the lullaby - she was a little horse
"""

print("Hello")
a=input("Do you want riddles or jokes: ").lower()
#code for riddles
while 1:    
    if a == "riddles":
        print("Ok starting,")
        r1=input("What you take to eat but dont eat?: ").lower()
        if r1=="plate":
            print("Correct answer")
        else:
            print("Wrong answer")
        playmore=input("Do you want to play more y/n: ").lower()
        if playmore=="y":
            print("Sowing Next")
            r2=input("If a red house is made up of red bricks, blue house of blue then what is a green house made up of?: ").lower()
            if r2=="glass":
                print("Correct answer")
            else:
                print("Wrong answer")
            playmore=input("Do you want to play more y/n: ").lower()
            if playmore=="y":
                print("Sowing Next")
                r3=input("What has foot on each side and one in the middle?").lower()
                if r3 == "yardstick":
                    print("Correct answer")
                else: 
                    print("Wrong answer")
                print("Riddles are over thank you for playing")
            else:
                break
                
        else:
            break

#now for jokes

    elif a=="jokes":
        print("Showing jokes")
        print("Why was 6 afraid of 9 on new year eve - because 9,8,7")
        playmore=input("Do you want more jokes? y/n: ").lower()
        if playmore=="y":
            print("showing next")
            print("why couldnt pony sing the lullaby - she was a little horse ")
            playmore=input("Do you want more jokes? y/n: ").lower()
            if playmore=="y":
                print("Showing Next")
                print("Why did the nurse need a red pen at work - in case she needed to draw blood")
                print("Jokes are over thank you")
            else:
                break
        else:
            break

#end statment
end=input("Did you like our program y/n: ").lower()
if end=="y":
    print("Thank you for the nice feedback")
else: 
    print("We will try to improve it ")