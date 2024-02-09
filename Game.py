import math
import random
import sys
print("")
playagain=True
while playagain:
    value=int(input("enter the value:\n1. for rock\n2. for paper or\n3. for scissors"))
    if value <1 or value>3:
        print(sys.exit("invalid choice! you should pick 1,2 or 3"))
    computer=int(random.choice("123"))
    print("you chose" +" ", value)
    print("and python choice is" + " ",computer)
    print(math.pi)
    print()
    if value==1  & computer==2:
        print("you win!")
    elif value==3 & computer==2:
        print("You win!")
    elif value==1 & computer==3:
        print("You win!")
    elif value==computer:
        print("Game tie!")
    else:
        print("Python wins!")
    playagain=input("\nYou want to continue playing?\nY.yes\nQ.quit")
    if playagain.lower()=="y":
        continue
    else:
        print("\nThank you for playing!")
        break
sys.exit("byee")
        


