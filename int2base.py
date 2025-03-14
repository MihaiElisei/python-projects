# Base Conversion Utility: Convert between decimal and bases (2-16)

BASE_DIGITS = '0123456789abcdef'

def int_to_base(my_int, my_base):
    """ 
    Converts a given integer to a specified base (2-16).
    
    This method repeatedly divides the integer by the base and stores the remainder.
    The final base representation is obtained by reading remainders from bottom to top.

    Example: Convert 8 to base 2 (binary)
    1.  8 / 2 = 4 remainder 0
    2.  4 / 2 = 2 remainder 0
    3.  2 / 2 = 1 remainder 0
    4.  1 / 2 = 0 remainder 1
    Result (bottom-up): 1000

    :param my_int: Integer to convert.
    :param my_base: Target base (2-16).
    :return: Converted value as a string.
    """
    print(f"Converting {my_int} to base {my_base}")

    if my_int == 0:
        return "0"

    base_str = ''
    my_quotient = my_int

    while my_quotient > 0:
        base_digit = BASE_DIGITS[my_quotient % my_base]  # Get corresponding base digit
        base_str = base_digit + base_str  # Append to result
        my_quotient //= my_base  # Reduce quotient

    print(f"The base {my_base} representation of {my_int} is {base_str}")
    return base_str


def base_to_int(base_str, my_base):
    """ 
    Converts a value from a given base (2-16) to decimal (base 10).
    
    This method applies the positional notation formula:
    Least significant digit * base^0 + next digit * base^1 + ...

    Example: Convert "3f" from base 16 to decimal
    (f = 15, 3 = 3) => (15 * 16^0) + (3 * 16^1) = 15 + 48 = 63

    :param base_str: Base representation as a string.
    :param my_base: The original base of the input string.
    :return: Converted integer.
    """
    print(f"Converting {base_str} from base {my_base} to decimal")

    answer = 0
    power = 0

    for char in reversed(base_str):  # Process digits from right to left
        int_equivalent = BASE_DIGITS.index(char)  # Get integer value of digit
        answer += int_equivalent * (my_base ** power)
        power += 1  # Increase exponent

    print(f"{base_str} base {my_base} to integer is {answer}")
    return answer


def is_valid_base(my_base):
    """ 
    Checks if the provided base is valid (between 2 and 16).

    :param my_base: Base value in string format.
    :return: True if valid, False otherwise.
    """
    if not my_base.isdigit():
        print("Error: You must enter a valid integer for the base.")
        return False
    if int(my_base) not in range(2, 17):
        print("Error: Base must be between 2 and 16.")
        return False
    return True


# User Interaction Menu
option_str = ""
while option_str != "0":
    print("\nInteger to Base Converter")
    print("-------------------------")
    print("1 - Convert from decimal to base x")
    print("2 - Convert from base x to decimal")
    print("0 - Exit the program")

    option_str = input("Enter your choice: ")

    if option_str not in "012":
        print("Error: Please enter a valid choice (0, 1, or 2).")

    elif option_str == "1":  # Decimal to Base Conversion
        int_str = input('Enter an integer to convert: ')

        if not int_str.isdigit(): 
            print("Error: You must enter a valid integer.")
            continue

        my_int = int(int_str)

        base_str = input('Enter the target base: ')

        if not is_valid_base(base_str):
            continue

        my_base = int(base_str)
        my_answer = int_to_base(my_int, my_base)
        print("Converted result:", my_answer)

    elif option_str == "2":  # Base to Decimal Conversion
        base_str = input('Enter a string to convert: ')

        if not all(char in BASE_DIGITS for char in base_str.lower()):  
            print("Error: Invalid characters detected in input.")
            continue

        base = input('Enter the original base: ')

        if not is_valid_base(base):  
            continue

        my_base = int(base)
        my_answer = base_to_int(base_str.lower(), my_base)
        print("Converted result:", my_answer)

    elif option_str == "0":
        print("\nExiting... Goodbye!")