# Program: dicesimulator

# Importing the random module for dice simulation
import random

# Defining a constant for the number of sides on a die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their values
    """
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    total = die1 + die2  # Calculating total of both dice
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    die1 = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")  # Shows initial value of die1 in main()

    # Calling roll_dice() function 3 times
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"die1 in main() is: {die1}")  # Checking die1 after function calls

# Calling main function
if __name__ == '__main__':
    main()
