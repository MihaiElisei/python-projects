import random
import time

# Define constants for the math quiz
OPERATORS = ["+", "-", "*"]  # Possible mathematical operations
MIN_OPERAND = 3  # Minimum value for operands
MAX_OPERAND = 12  # Maximum value for operands
TOTAL_PROBLEMS = 10  # Number of problems to solve

# Function to generate a random math problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate right operand
    operator = random.choice(OPERATORS)  # Randomly select an operator
    
    expr = str(left) + " " + operator + " " + str(right)  # Create the math expression
    answer = eval(expr)  # Compute the answer (safe in this context)
    return expr, answer

wrong = 0  # Track the number of incorrect answers
input("Press any key to start!")  # Prompt user to start the quiz
print("---------------------------")

start_time = time.time()  # Record start time

# Loop through the set number of problems
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Generate a new problem
    while True:
        guess = input(f"Problem #{i+1}: {expr} = ")  # Prompt user for an answer
        if guess == str(answer):  # Check if the answer is correct
            break  # Exit the loop if correct
        wrong += 1  # Increment wrong answer counter if incorrect
        
end_time = time.time()  # Record end time

total_time = round(end_time - start_time, 2)  # Calculate total time taken
print("---------------------------")
print(f"Nice work! You finished in {total_time} seconds!")  # Display completion message