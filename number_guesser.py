import random  # Import the random module for generating random numbers

# Ask the user to input the upper limit of the number range
top_of_range = input("Type a number: ")
guesses = 0  # Initialize the guess counter

# Check if the input is a valid number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # Convert input to an integer
    
    # Ensure the number is greater than 0
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()  # Exit the program
else:
    print("Please type a number next time.")
    quit()  # Exit the program

# Generate a random number between 0 and the chosen upper limit
random_number = random.randint(0, top_of_range)

# Start the guessing loop
while True:
    guesses += 1  # Increment the guess counter
    user_guess = input("Make a guess: ")
    
    # Check if the input is a valid number
    if user_guess.isdigit():
        user_guess = int(user_guess)  # Convert input to an integer
    else:  
        print("Please type a number next time.")
        continue  # Skip to the next loop iteration
    
    # Check if the user's guess is correct
    if user_guess == random_number:
        print("You got it!")  # User guessed correctly, exit loop
        break
    elif user_guess > random_number:
        print("You were above the number")  # Hint for too high guesses
    else: 
        print("You were below the number")  # Hint for too low guesses

# Print the number of attempts it took to guess correctly
print(f"You got it in {guesses} guesses")