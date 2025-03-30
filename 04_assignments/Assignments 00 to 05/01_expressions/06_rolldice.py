import random  # Import the random module to simulate rolling dice

# Number of sides on each die
NUM_SIDES = 6  

def main():
    # Roll two dice (randomly generate numbers between 1 and NUM_SIDES)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # Calculate the total of both dice
    total = die1 + die2

    # Print the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# This line ensures the main() function runs when the program is executed
if __name__ == "__main__":
    main()
