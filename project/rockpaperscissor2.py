import random

print("Welcome to the game Rock Paper Scissor")
print("Here are the following rules: \nRock beats Scissor \nPaper beats Rock \nScissor beats Paper")


while True:

    def player_selection():
        user_action = str(input("Pick a choice (Rock, Paper, Scissor) please:"))
        print("Your choice is:", user_action)
        return user_action

    def computer_selection():
        possible_ai_actions = ["Rock", "Paper", "Scissor"]
        computer_action = random.choice(possible_ai_actions)
        print("AI's choice is:", computer_action)
        return computer_action

    def determine_winner(user_action, computer_action):
        
        if user_action == computer_action:
            print("It's a tie!")
        elif user_action == "Rock":
            if computer_action == "Scissor": print("You win!")
            if computer_action == "Paper": print("You lose!")
        elif user_action == "Paper":
            if computer_action == "Rock": print("You win!")
            if computer_action == "Scissor": print("You lose!")
        elif user_action == "Scissor":
            if computer_action == "Paper": print("You win!")
            if computer_action == "Rock": print("You lose!")
        else: print("Please make sure your spelling is correct!")

    determine_winner(player_selection(), computer_selection())

    play_again = input("Would you like to play again? Y or N:")
    if play_again == "Y":
        True
    elif play_again =="N": 
        print("Let's play next time!") 
        break
    else: print("Please enter Y or N")

