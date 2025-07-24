import random
initial_score=0
while True:
    choice_entered=input("Enter your choice (rock,paper,scissor) : ")
    
    print("User's choice is : ",choice_entered)
    choices=['rock','paper','scissor']
    computer_choice=random.choice(choices)
    print("Computer's choice : ",computer_choice)
    if(choice_entered!='rock' and choice_entered!='paper' and choice_entered!='scissor'):
        print("INVALID CHOICE")

    if(choice_entered==computer_choice):
        print("")
        print("IT'S A TIE!")
        print("")


    elif(choice_entered=='rock' and computer_choice=='scissor'
     or choice_entered=='paper' and computer_choice=='rock'
     or choice_entered=='scissor' and computer_choice=='paper'):
        print("")
        print("YOU WON!")
        print("")
        initial_score=initial_score+1

    else:
        print("")
        print("YOU LOSE!")
        print("")
    ch=input("Do you want to play again?")
    if ch=='n':
        print("THANK YOU! and your final score is : ",initial_score)
        break