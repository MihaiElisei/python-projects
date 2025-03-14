# Number Classification: Perfect, Abundant, or Deficient

def classify_number(number):
    """
    Classifies a number as perfect, abundant, or deficient based on the sum of its divisors.
    
    A perfect number: Sum of its proper divisors equals the number itself.
    An abundant number: Sum of its proper divisors is greater than the number.
    A deficient number: Sum of its proper divisors is less than the number.

    :param number: The number to classify.
    :return: A string indicating the classification.
    """
    sum_of_divisors = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    if sum_of_divisors == number:
        return "perfect"
    elif sum_of_divisors > number:
        return "abundant"
    else:
        return "deficient"


def main():
    """
    Main function that prompts the user for an upper range and classifies all numbers from 2 to the upper limit.
    """
    # Get user input for the range limit
    top_num_str = input("Enter the upper limit for the range: ")

    # Validate input: Check if it's a valid integer
    if not top_num_str.isdigit():
        print(f"Error: '{top_num_str}' is not a valid integer. Exiting...")
        quit(1)

    top_num = int(top_num_str)

    # Ensure the range starts from at least 2
    if top_num < 2:
        print(f"Error: Upper limit must be at least 2. Exiting...")
        quit(1)

    # Loop through numbers from 2 to the specified limit and classify each
    for number in range(2, top_num + 1):
        classification = classify_number(number)
        print(f"{number} is {classification}")


# Run the script
if __name__ == "__main__":
    main()