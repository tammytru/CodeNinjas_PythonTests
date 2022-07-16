#----- Paper, Rock, Scissors (EASY) -----#

import random
options = ['p', 'r', 's']
winningScore = 3

compScore = 0
plrScore = 0

while True:
    plr = input("Enter your choice ('P' 'R' 'S' 'quit'): ")
    comp = random.choice(options)
    print("Computer played:", comp.upper())

    if plr == 'quit':
        break
    elif plrScore == winningScore:
        print("YOU WIN!")
        break
    elif compScore == winningScore:
        print("YOU LOSE")
        break

    print("Computer:", compScore)
    print("Player:", plrScore)
    print("-----------------------")

    if comp == 'p':
        if plr.lower() == 'p':
            print("Draw")
        elif plr.lower() == 'r':
            compScore += 1
            print("Point to Computer")
        elif plr.lower() == 's':
            plrScore += 1
            print("Point to Player")
    elif comp == 'r':
        if plr.lower() == 'p':
            plrScore += 1
            print("Point to Player")
        elif plr.lower() == 'r':
            print("Draw")
        elif plr.lower() == 's':
            compScore += 1
            print("Point to Computer")
    else:
        if plr.lower() == 'p':
            compScore += 1
            print("Point to Computer")
        elif plr.lower() == 'r':
            plrScore += 1
            print("Point to Player")
        elif plr.lower() == 's':
            print("Draw")