import random
import sys
import subprocess
subprocess.call('clear')
generatedNum=random.randint(0,50)
count=0
while True:
    print("Enter your guessed number:")
    guessedNum=int(input(">"))
    count=count+1
    if(count!=4):
        if (generatedNum==guessedNum):
            print(generatedNum)
            print("Your guess is right")
            sys.exit()
        else:
            if(guessedNum>generatedNum):
                print("Too High")
            else:
                print("Too less")
    elif (count==4):
        print("Too many attempts")
        print("Right Answer is",generatedNum)
        sys.exit()  