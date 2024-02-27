import random

def roll():  # Rolling the dice
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

players_scores = []     # Score Card
c = 0

while True:  # Players
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            players_scores = [0] * players
            break
        else:
            print("Must be (2-4)")
    else:
        print("Must be an integer!")

while True:     # Game script
    for player in range(players):       #For the turn of each player
        player_turn = player + 1
        print(f"\nPlayer number {player_turn}'s turn has just started.\n")
        while True:     #Game script for a player
            print(f"Your total score is {players_scores[player]}")
            user_decision = input("Do you want to roll the dice? (y): ")
            if user_decision != 'y':        #User decision to play or not.
                break
            
            value = roll()      #Rolling the dics for value
            if value == 1:      #If 1, then player's score == 0
                players_scores[player] = 0
                print(f"You rolled a 1. Turn done!\nYour total score is {players_scores[player]}")
                break

            players_scores[player] += value
            if players_scores[player] >= 20:        #Checking if player won or not.
                print(f"You rolled a {value}.")
                break
            print(f'You rolled a {value}. Your current score is {players_scores[player]}')

        if players_scores[player] >= 20:        #Wining player announcement.
            print(f"Player number {player_turn} has won the match with a score of {players_scores[player]}")
            c = 1
            break

    if c == 1:
        break
