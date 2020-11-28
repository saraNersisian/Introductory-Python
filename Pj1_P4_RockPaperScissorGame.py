#Sara Nersisian
#CS 1260
#Project 1 - Problem 4
#11/14/2020


import sys
import random
print("\n************ Rock, Paper, Scissor Game ************ ")
choices = ["Rock", "Paper","Scissor"]
playAgain = 'y'

while(playAgain=='y'):
    print("Computer turn... ")
    computer = random.choice(choices)
    print("[Hidden choice]")
    user = input ("User turn... \n")
    
    if computer == "Rock" and (user =="Scissor" or user =="scissor") :
        statment = "Rock smashes scissors"
        winner = "Computer"
    elif (user == "Rock" or user == "rock") and computer =="Scissor" :
        statment ="Rock smashes scissors"
        winner = "User"
    elif computer == "Scissor" and (user =="Paper" or user =="paper") :
        statment ="Scissors cut paper"
        winner = "Computer"
    elif user == ("Scissor" or user == "scissor" ) and computer =="Paper" :
        statment = "Scissors cut paper"
        winner = "User"
    elif computer == "Paper" and (user =="Rock" or user =="rock" ) :
        statment ="Paper wraps rock"
        winner = "Computer"
    elif (user == "Paper" or user == "paper" )and computer =="Rock" :
        statment ="Paper wraps rock"
        winner = "User"
    elif computer == user:
        print("Computer choice was also " , computer)
        print("Tied Game! Start again")
        sys.exit()
    else:
        print("Invalid Inputs! \nExiting the program...")
        sys.exit()
        
    print("\n<<======== RESULTS =========>>" )
    print("Computer choice: " , computer)
    print("User choice: ", user)
    print(statment)
    print("\n******** WINNER *******")
    print (winner)

    playAgain = input("Continue Playing (y/n)? ")
    if(playAgain=='n'):
        print("Exiting the program...")
        sys.exit()
    