# Convert an integer to binary and vice versa

# Integer to Binary Conversion
int_str = input('Give me an int: ')  # Prompt user for an integer input
my_int = int(int_str)  # Convert input string to an integer

bin_str = ''  # Initialize an empty string to store binary representation
while my_int > 0:  
    my_remainder = my_int % 2  # Get remainder when divided by 2 (binary digit)
    my_int = my_int // 2  # Reduce the integer by dividing it by 2
    bin_str = str(my_remainder) + bin_str  # Append remainder to the left of the binary string

print('The binary of', int_str, 'is', bin_str)  # Output binary representation

# Binary to Integer Conversion
print('\nBinary to int')
bin_str = input('Give me a binary string: ')  # Prompt user for binary input

# First method: Manual binary-to-integer conversion using powers of 2
temp = bin_str  # Copy binary string
new_int = 0  # Initialize integer result
power = 0  # Power counter (starts at 0 for the least significant bit)

while len(temp) > 0:  
    bit = int(temp[-1])  # Take the last character (rightmost bit)
    new_int = new_int + bit * 2 ** power  # Multiply by 2^power and add to result
    temp = temp[:-1]  # Remove the last character from temp
    power += 1  # Increment power for the next bit

print(bin_str, 'to integer is', new_int)  # Output converted integer

# Second method: Alternative binary-to-integer conversion using a loop
new_answer = 0  # Initialize integer result
for e in bin_str[:-1]:  # Iterate through all bits except the last one
    new_answer += new_answer + (int(e) * 2)  # Shift left and add current bit
new_answer += int(bin_str[-1])  # Add the last bit

print(f"Alternative algorithm: {bin_str} to int is {new_answer}")  # Output result