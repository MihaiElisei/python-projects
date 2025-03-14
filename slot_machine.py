"""
Slot Machine Game

This program simulates a slot machine where users can deposit money, place bets, and spin to win. 
Players can bet on multiple lines, and winnings are based on symbol values.

"""

import random

# Constants for betting limits and slot machine dimensions
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol frequency and values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """Checks for winning lines and calculates winnings based on bet and symbol values."""
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # Check the symbol in the first column of the line
        for column in columns:
            if column[line] != symbol:
                break  # Stop checking if symbols do not match
        else:
            winnings += values[symbol] * bet  # Calculate winnings
            winning_lines.append(line + 1)  # Store the winning line number
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """Generates a random slot machine spin based on symbol probabilities."""
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = []  
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Copy of the symbol list
        
        for _ in range(rows):
            value = random.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)  # Remove selected symbol to prevent repetition
            column.append(value)  # Add symbol to the column
            
        columns.append(column)  # Add column to the slot machine
    
    return columns


def print_slot_machine(columns):
    """Prints the slot machine output in a formatted way."""
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))


def deposit():
    """Prompts the user to deposit money and ensures a valid amount is entered."""
    while True:
        amount = input("What amount would you like to deposit? $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount greater than 0.")


def get_number_of_lines():
    """Gets the number of lines the user wants to bet on, ensuring it is within range."""
    while True:
        lines = input(f"Enter the number of lines to bet on [1-{MAX_LINES}]: ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Please enter a valid number of lines.")


def get_bet():
    """Prompts the user for the bet amount per line and ensures it is within limits."""
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")


def spin(balance):
    """Handles a single spin, checking for sufficient balance and processing winnings."""
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Insufficient funds! Your current balance is ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"Winning lines: {', '.join(map(str, winning_lines))}")
    
    return winnings - total_bet


def main():
    """Main function to run the slot machine game."""
    balance = deposit()
    while balance > 0:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to play or 'q' to quit: ")
        if answer.lower() == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}.")

# Start the game
main()
