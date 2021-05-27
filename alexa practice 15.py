rice=("Rice, (Oryza sativa), edible starchy cereal grain and the grass plant (family Poaceae) by which it is produced. ... Rice is cooked by boiling, or it can be ground into a flour. It is eaten alone and in a great variety of soups, side dishes, and main dishes in Asian, Middle Eastern, and many other cuisines.")
wheat=("Wheat is a grass widely cultivated for its seed, a cereal grain which is a worldwide staple food. The many species of wheat together make up the genus Triticum; the most widely grown is common wheat (T. aestivum). ... Botanically, the wheat kernel is a type of fruit called a caryopsis.")
blackgram=("Black gram (Vigna mungo (L.) Hepper) is an erect, fast-growing annual, herbaceous legume reaching 30-100 cm in height. It has a well-developed taproot and its stems are diffusely branched from the base.")
quest = input("enter a food grain between rice, wheat and black gram: ")

if quest == "rice":
    print("the information is :"+ rice)
elif quest =="wheat":
    print ("the info is : "+wheat)
elif quest == "black gram":
    print("the info is : " + blackgram)
else:
    print("the grains name is not stored in this program")