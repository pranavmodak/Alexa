bill = 0
print("Five items are : 1. Chocolate, 2.Pizza, 3. Burger, 4. Pasta, 5. Noodles")
print("The price  are: 1. Rs 10, 2.Rs 100 3.Rs 110 4.Rs 120 5. Rs 90")
while 1:
    q1=input("Enter a item nunber: ")
    q2=int(input("Enter quantity: "))
    
    if q1 == "1":
        print("Item added to the cart ")
        bill=bill+q2*10
    
    elif q1 == "2":
        print("Item added to the cart ")
        bill=bill+q2*100
    
    elif q1 == "3":
        print("Item added to the cart ")
        bill=bill+q2*110
    
    elif q1 == "4":
        print("Item added to the cart ")
        bill=bill+q2*120
    
    elif q1 == "5":
        print("Item added to the cart ")
        bill=bill+q2*90
    
    else:
        print("This item is not valid")
    
    a=input("Do you want to continue yes/ no: ").lower()
    if a=="yes":
        print("Ok")
    else:
        print("You bill is: Rs "+ str(bill))
        break