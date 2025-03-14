# Print a welcome message for the quiz
print("Welcome to my computer quiz!")

# Ask the user if they want to play
playing = input("Do you want to play? [y/n] ")
score = 0  # Initialize the score variable

# Check if the user does not want to play
if playing.lower() != "y":
    quit()  # Exit the program if the user inputs anything other than "y"

print("Okay! Let's play 🙂")  # Confirmation message to start the game

# Ask the first question
answer = input("What does CPU stand for? ")

# Check if the answer is correct
if answer.lower() == "central processing unit":
    print("Correct!")  # Inform the user they got it right
    score += 1  # Increase the score
else: 
    print("Incorrect!")  # Inform the user they got it wrong

# Ask the second question
answer = input("What does GPU stand for? ")

# Check if the answer is correct
if answer.lower() == "graphics processing unit":
    print("Correct!")  
    score += 1  
else: 
    print("Incorrect!")  

# Ask the third question
answer = input("What does RAM stand for? ")

# Check if the answer is correct
if answer.lower() == "random access memory":
    print("Correct!")  
    score += 1  
else: 
    print("Incorrect!")  

# Ask the fourth question
answer = input("What does PSU stand for? ")

# Check if the answer is correct (Note: There's a typo in "power supply unit")
if answer.lower() == "power supply unit": 
    print("Correct!")  
    score += 1  
else: 
    print("Incorrect!")  

# Display the final score
print(f'Your total score is: {score}')