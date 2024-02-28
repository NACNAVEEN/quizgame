print("Welcome to quiz mania")

playing=input("Do you want to play? ")
score=0
if playing !="yes":
    quit()
    
print("Okay! Lets play the game guys")

answer=input("What does VLSI stands for? ")
if answer=="verilog":
    print("Correct<#>")
    score+=1
else:
    print("Incorrect!")
    
answer=input("tell any one of the library in ML? ")
if answer=="Numpy":
    print("Correct")
    score+=1
else:
    print("Incorrect!")
    
answer=input("what is the packages availabke in python? ")
if answer=="pip":
    print("Correct")
    score+=1
else:
    print("Incorrect!")

answer=input("what is the tools for the embedded system? ")
if answer=="Arduino":
    print("Correct")
    score+=1
else:
    print("Incorrect!")
    
print("you got" + str(score) +"questioned answered correctly")
print("you got" + str((score/4)*100) +"%")