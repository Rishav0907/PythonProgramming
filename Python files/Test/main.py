import random
while True:
    print("rock")
    print("papers")
    print("scissors")
    print("Player 1's choice ----")
    pl1=str(input(">"))
    comp=random.randrange(0,4)
    if comp==1:
        print("comp choosed rock")
    elif comp==2:
        print("Comp choosedpapers")
    else:
        print("Comp choosed scissors")
    if pl1=="rock" or pl1=="rocks":
        if comp==2:
            print("Computer wins")
        elif comp==3:
            print("player wins")
        else:
            print("Its a tie")

    if pl1=="paper" or pl1=="papers":
        if comp==1:
            print("Player wins")
        elif comp==3:
            print("Its a tie")
        else:
            print("Computer wins")
    if pl1=="scissor" or pl1=="scissors":
        if comp==1:
            print("Computer wins")
        elif comp==3:
            print("Player wins")
        else:
            print("Its a tie")