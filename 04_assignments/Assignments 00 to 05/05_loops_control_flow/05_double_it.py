# Ask user to enter a number
curr_value = int(input("Enter a number: "))

# Double the number until it reaches 100 or more
while curr_value < 100:
    curr_value *= 2  # Double the value
    print(curr_value, end=" ")  # Print the new value on the same line
