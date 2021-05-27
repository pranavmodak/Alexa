score = 0
print("we are going to do  a quiz")
q1=input("what is capital of america options washington dc and new york: ")
if q1 == "washington dc":
    print("correct ans")
    score=score+1
else:
    print("wrong ans")
    
q2=input("who is no1 cricketer in odi options baber azam and virat kohli: ")
if q2=="baber azam ":
    print("correct answer")
    score=score+1
else:
    print("wrong ans")

q3=input("who is no1 cricketer in test options rohit sharma and kane williamsan: ")
if q3=="kane williamson":
    print("correct answer")
    score=score+1
else:
    print("wrong answer")
    
print("the correct answers you have given are: "+ str(score))