# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 16:45:13 2021

@author: modak_ng8awn0
"""
bill=0
while 1:
    print("1. Butterscotch - Rs. 180")
    print("2. Vanila - Rs. 100")
    print("3. Mango – Rs. 150")
    print("4. Strawberry – Rs. 120")
    print("5. ChocoChips – Rs. 200")
    
    q1=input("enter number of the flavor: ").lower()
    q2=int(input("enter thhe quantity"))

    if q1 == "1":
        print("Item added to the cart ")
        bill=bill+q2*180
    
    elif q1 == "2":
        print("Item added to the cart ")
        bill=bill+q2*100
    
    elif q1 == "3":
        print("Item added to the cart ")
        bill=bill+q2*150
    
    elif q1 == "4":
        print("Item added to the cart ")
        bill=bill+q2*120
    
    elif q1 == "5":
        print("Item added to the cart ")
        bill=bill+q2*200
    
    else:
        print("This item is not valid")
        
    a=input("Do you want to continue yes/ no: ").lower()
    if a=="yes":
        print("Ok")
    else:
        print("You bill is: Rs "+ str(bill))
        break
