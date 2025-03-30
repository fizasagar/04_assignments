# Constant for the maximum value
MAX_VALUE = 10000

# Initialize first two Fibonacci numbers
a, b = 0, 1

# Print Fibonacci sequence up to MAX_VALUE
while a < MAX_VALUE:
    print(a, end=" ")  # Print the current term
    a, b = b, a + b  # Update the values for the next term
