import random

CHOICES = ['rock', 'paper', 'scissors']

def determine_winner(player_choice, computer_choice):
    outcomes = {
        'rock': {'scissors'},
        'paper': {'rock'},
        'scissors': {'paper'}
    }

    if player_choice == computer_choice:
        return "tied"
    elif computer_choice in outcomes[player_choice]:
        return "won"
    else:
        return "lost"

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def main():
    player_wins = 0
    computer_wins = 0
    
    while True:
        player_choice = input("Please enter your choice of rock, paper, or scissors").lower()
        if player_choice not in CHOICES:
            print("That was not a valid option")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        
        match result:
            case "won":
                player_wins += 1
            case "lost":
                computer_wins += 1
            case _:
                pass
    
        print(f"You have {result}!")
        print(f"The standings are {computer_wins} computer wins, {player_wins} player wins")

main()
