import random

def get_choices():
        player_choice = input("Enter a choice (rock,paper,scisscors)")
        option = ["rock","paper","scissors"]
        computer_choice = random.choice(option)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices

def check_win(player,computer):
        print(f"You chose {player}, computer chose {computer}")
        if player == computer:
                return "its a tie!"
        elif player =="rock":
            if computer =="scissors":
                return "Rock smashes scissors ! You win!"
            else:
                return "Paper Covers rock ! You lose."
        elif player =="paper":
            if computer =="rock":
                return "Paper Covers rock ! You win!"
            else:
                return "Scissors cut paper ! You lose."
        elif player =="Scissors":
            if computer =="paper":
                return "Scissors cut paper ! You win!"
            else:
                return "Rock smashes scissors ! You lose."
choices =get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
