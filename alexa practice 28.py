while 1:
    a=int(input("enter a number: "))
    b=input("enter for which you want to convert l-ml, m-cm and kg-g: ").lower()

    if b=="l-ml":
        print("the conversion is :"+ str(a*1000))
    elif b=="m-cm":
        print("the conversion is :"+ str(a*100))
    elif b=="kg-g":
        print("the conversion is :"+ str(a*1000))
    else:
        print("item not valid")
    c=input("do you want to continue: ").lower()
    if c=="yes":
        print("ok")
    else:
        break