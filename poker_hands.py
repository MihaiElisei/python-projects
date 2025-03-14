"""
Poker Hand Frequency Analysis

This program analyzes a dataset of poker hands from a file and calculates the frequency of each type of poker hand.
It also compares the actual occurrence rates with expected theoretical probabilities.

How It Works:
1. Reads the poker hands dataset from a file (`poker-hand-testing.data`).
2. Parses each line to extract the final hand ranking.
3. Counts occurrences of each hand type.
4. Calculates the percentage occurrence of each hand type.
5. Compares actual probabilities to expected probabilities.
6. Displays the results in a well-formatted table, including an ASCII bar chart for visualization.

"""

from collections import Counter

# Define rank names for poker hands
RANK_LIST = ['nothing', 'pair', 'two pair', 'three of a kind', 'straight', 'flush', 
             'full house', 'four of a kind', 'straight flush', 'royal flush']

# Expected probabilities in a fair dataset (approximate based on poker odds)
EXPECTED_PROBABILITIES = [50.1, 42.3, 4.75, 2.11, 0.39, 0.20, 0.14, 0.024, 0.0014, 0.000154]


def read_poker_file(filename):
    """
    Reads the poker hand dataset line by line.
    
    :param filename: The name of the file to read.
    :return: A list of lines from the file.
    """
    try:
        with open(filename, 'r') as fh:
            return fh.readlines()  # Read line-by-line (better memory management)
    except IOError as e:
        print(f"Error reading file: {e}")
        quit()


def process_poker_hands(lines):
    """
    Processes poker hands from the dataset and counts occurrences of each hand rank.

    :param lines: A list of lines containing poker hands.
    :return: A Counter dictionary with hand rank frequencies.
    """
    rank_counts = Counter()

    for line in lines:
        try:
            # Extract the last value (hand rank) and convert to integer
            hand_rank = int(line.strip().split(',')[-1])
            rank_counts[hand_rank] += 1  # Increment count
        except ValueError as e:
            print(f"Skipping invalid line: {line.strip()} -> {e}")
            continue

    return rank_counts


def display_statistics(rank_counts):
    """
    Displays the total number of hands, probabilities, and a comparison to expected probabilities.
    
    :param rank_counts: A Counter dictionary with hand rank frequencies.
    """
    total_count = sum(rank_counts.values())  # Compute total hands

    print(f"\nTotal hands in file: {total_count:,d}")
    print("=" * 50)
    print(f"{'Hand Type':18s} {'Count':>10s} {'Actual %':>10s} {'Expected %':>10s} {'Variance':>10s}")
    print("=" * 50)

    for i, rank_name in enumerate(RANK_LIST):
        count = rank_counts.get(i, 0)  # Get count or default to 0
        actual_prob = (count / total_count) * 100 if total_count > 0 else 0
        expected_prob = EXPECTED_PROBABILITIES[i]
        variance = actual_prob - expected_prob  # Difference from expected probability

        print(f"{rank_name:18s} {count:10,d} {actual_prob:9.2f}% {expected_prob:9.2f}% {variance:9.2f}%")

    print("=" * 50)


def display_bar_chart(rank_counts, total_count, max_bar_length=50):
    """
    Displays a simple ASCII bar chart for hand frequency visualization.

    :param rank_counts: A Counter dictionary with hand rank frequencies.
    :param total_count: Total number of poker hands.
    :param max_bar_length: Maximum length of the bar in characters.
    """
    print("\nHand Frequency Distribution (ASCII Chart):")
    print("=" * 50)

    for i, rank_name in enumerate(RANK_LIST):
        count = rank_counts.get(i, 0)
        percentage = (count / total_count) * 100 if total_count > 0 else 0
        bar_length = int((count / total_count) * max_bar_length)  # Scale bar length
        bar = "█" * bar_length  # Unicode block for better visualization

        print(f"{rank_name:18s} | {bar} {percentage:6.2f}%")

    print("=" * 50)


def main():
    """
    Main function to read, process, and display poker hand statistics.
    """
    filename = "poker-hand-testing.data"
    poker_lines = read_poker_file(filename)  # Read file

    rank_counts = process_poker_hands(poker_lines)  # Process hands

    display_statistics(rank_counts)  # Show numerical stats
    display_bar_chart(rank_counts, sum(rank_counts.values()))  # Show ASCII chart


if __name__ == "__main__":
    main()