import random  # Import the random module for generating random choices

# Initialize win counters for user and computer
user_wins = 0
computer_wins = 0

# List of possible choices
options = ["rock", "paper", "scissors"]

# Start the game loop
while True:
    # Ask the user to input their choice
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    # If the user wants to quit, exit the loop
    if user_input == "q":
        break
    
    # Check if the input is valid (rock, paper, or scissors)
    if user_input not in options:
        continue  # If not, restart the loop and ask again
    
    # Computer randomly selects rock, paper, or scissors
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f'Computer picked: {computer_pick}.')

    # Determine the winner
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1  # Increase user win count
        continue  # Skip to next iteration
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1  
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1  
    
    else:
        print("You lost!")  # If none of the above conditions met, user loses
        computer_wins += 1  # Increase computer win count

# Display final results after the game ends
print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")