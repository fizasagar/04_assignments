# Project : Guess the number by User

import random
print("Guess the number between 1 to 100!")
number = random.randint(1, 100)  # Random number generate hoga
attempts = 0  # Score tracker (counting attempts)

while True:
    guess = int(input("Enter your guess number: "))
    attempts += 1  # Har guess par count badhayega

    if guess < number:
        print("Too Low Number!")
    elif guess > number:
        print("Too High Number!")
    else:
        print(f"Congratulations! You Got The Right Number in {attempts} attempts.")
        break 
