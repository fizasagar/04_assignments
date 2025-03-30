# Define the affirmation
correct_affirmation = "I am capable of doing anything I put my mind to."

while True:
    # Prompt user for input
    user_input = input("Please type the following affirmation: ")
    
    # Check if input matches the affirmation
    if user_input == correct_affirmation:
        print("That's right! :)")
        break  # Exit loop once correct
    else:
        print("Hmmm, that was not the affirmation. Try again.")
