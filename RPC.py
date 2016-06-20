# RockPaperScissors.py
# Zachary Moffatt
# 6/18/16

import re, sys, random

#printChoice(num)
#Takes in a number represent rock,paper,or sissors
#Returns the name of the choice
def printChoice(num):
    if(num==1):
        return"rock"
    elif(num==2):
        return"paper"
    else:
        return"sissors"

#Main
print('Do you wish to play Rock Paper Sissors? (y/n)')
while 1==1:
    choice = input()

    yesRegEx = re.compile('yes|y|Yes')
    noRegEx = re.compile('no|n|No')

    if(noRegEx.match(choice)):
        print("Thank you for playing")
        #Try and remove traceback from exit
        sys.exit(0)

    if(yesRegEx.match(choice)):
        print("Let's get started!")
        break;
    else:
        print("I'm sorry, I didn't understand what you said there. Please try again")

#Game proper
print("Lets play for best two out of three\n")
input()
player = 0
computer = 0
roundNum = 1

rockRegEx = re.compile('rock|r|R|Rock')
paperRegEx = re.compile('paper|p|P|Paper')
sissorsRegEx = re.compile('sissors|s|S|Sissors')

# 1 represents rock, 2 paper, 3 sissors

while (player < 3 and computer < 3):

    #Generate computer's choice
    computerChoice = random.randint(1,3)

    #Get player's choice
    playerChoice = 0
    print("Round ", roundNum)
    print("Please enter 'rock', 'paper' or 'sissors'")
    while playerChoice == 0:
        hand = input()
        if(rockRegEx.match(hand)):
            playerChoice = 1
        elif(paperRegEx.match(hand)):
            playerChoice = 2
        elif(sissorsRegEx.match(hand)):
            playerChoice = 3
        else:
            print("I didn't understand your choice. Please try again")

    #Print player and computer choices
    print("You play:", printChoice(playerChoice), "\nComputer plays:", printChoice(computerChoice))

    #Check the win
    if(playerChoice == computerChoice):
        print("Tie!")
    else:
        if(playerChoice==1):
            if(computerChoice==2):
                computer+=1
                print("Computer wins!")
            if(computerChoice==3):
                player+=1
                print("Player wins!")
        elif(playerChoice==2):
            if(computerChoice==3):
                computer+=1
                print("Computer wins!")
            if(computerChoice==1):
                player+=1
                print("Player wins!")
        elif(playerChoice==3):
            if(computerChoice==1):
                computer+=1
                print("Computer wins!")
            if(computerChoice==2):
                player+=1
                print("Player wins!")
    roundNum+=1


#Game over
print("- - - - - - - - - - - - - - - - - - -")
if(player == 3):
    print("You Win!")
else:
    print("You Lose!")
print("- - - - - - - - - - - - - - - - - - -")