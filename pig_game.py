import random

# Function to simulate rolling a dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)  # Generate a random number between 1 and 6
    return roll

# Prompt for the number of players
while True:
    players = input("Enter the number of players [2-4]: ")
    
    if players.isdigit():  # Ensure input is a valid number
        players = int(players)
        if 2 <= players <= 4:  # Check if the number of players is within the valid range
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")
        
max_score = 50  # Set the winning score

# Initialize player scores with zero
player_scores = [0 for _ in range(players)]

# Main game loop, continues until a player reaches the max score
while max(player_scores) < max_score: 
    
    for player_index in range(players):
        print(f"\nPlayer number {player_index + 1} turn just started\n")  # Indicate which player's turn it is
        print(f"Your total score is {player_scores[player_index]}\n")  # Show current total score
        
        current_score = 0  # Reset current turn score
        while True:
            should_roll = input("Would you like to roll? [y]")  # Ask if the player wants to roll
            if should_roll.lower() != "y":  # Exit turn if player chooses not to roll
                break
            
            value = roll()  # Roll the dice
            
            if value == 1:  # If the player rolls a 1, they lose their turn points
                print("You rolled a 1! Turn done!")
                current_score = 0  # Reset turn score to 0
                break  # End turn
            else:
                current_score += value  # Add roll value to current score
                print(f"You rolled a {value}")  # Show rolled value
            
            print(f"Your score is {current_score}")  # Display current turn score
            
        player_scores[player_index] += current_score  # Add turn score to total score
        print(f"Your total score is {player_scores[player_index]}")  # Show updated total score

# Determine the winner
max_score = max(player_scores)  # Get the highest score
winning_idx = player_scores.index(max_score)  # Find the index of the winning player
print(f"Player number {winning_idx + 1} is the winner with the score of {max_score}")  # Announce the winner
