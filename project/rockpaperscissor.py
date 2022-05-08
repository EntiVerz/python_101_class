import random
import time

while True:

    time.sleep(0.5)
    print("Welcome to the game Rock Paper Scissor")
    time.sleep(1.5)
    print("Here are the following rules: \nRock beats Scissor \nPaper beats Rock \nScissor beats Paper")

    def player_action():

        time.sleep(2.7)
        user_choice = input("1 = Rock \n2 = Paper \n3 = Scissor \nPlease choose a number with their corresponding actions:")
        if user_choice == "1":
            time.sleep(1)
            user_choice = "Rock"
            print("You choice is Rock")
        elif user_choice == "2":
            time.sleep(1)
            user_choice = "Paper"
            print("Your choice is Paper")
        elif user_choice == "3":
            time.sleep(1)
            user_choice = "Scissor"
            print("Your choice is Scissor")
        else:
            time.sleep(1)
            print("Please enter numbers 1-3!")
            user_choice = player_action()
        return user_choice

    def ai_action():
        time.sleep(1)
        print("The computer is now choosing!")
        ai_choice = random.randint(1,3)
        if ai_choice == 1:
            time.sleep(1)
            print("Computer's choice is Rock")
            ai_choice = "Rock"
        elif ai_choice == 2:
            time.sleep(1)
            print("Computer's choice is Paper")
            ai_choice = "Paper"
        else:
            time.sleep(1)
            print("Computer's choice is Scissor")
            ai_choice = "Scissor"
        return ai_choice
    
    def determine_winner(user_choice, ai_choice):

        if user_choice == ai_choice:
            time.sleep(1)
            print("It's a tie!")
        elif user_choice == "Rock":
            time.sleep(1)
            if ai_choice == "Scissor": print("You win!")
            if ai_choice == "Paper": print("You lose!")
        elif user_choice == "Paper":
            time.sleep(1)
            if ai_choice == "Rock": print("You win!")
            if ai_choice == "Scissor": print("You lose!")
        elif user_choice == "Scissor":
            time.sleep(1)
            if ai_choice == "Paper": print("You win!")
            if ai_choice == "Rock": print("You lose!")
        else: 
            print("Please enter numbers 1 to 3!")

    determine_winner(player_action(), ai_action())

    play_again = input("Would you like to play again? Y or N:")

    if play_again.upper() == "Y" or "Y " or " Y":
        True
    elif play_again.upper() == "N" or "N " or " N":
        print("Let's play next time!") 
        break
    else: 
        print("Please input Y or N!")
        play_again = input("Would you like to play again? Y or N:")