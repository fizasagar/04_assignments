# Sentence starter for the Mad Libs game
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Get words from the user
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Create and print the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Run the main function
if __name__ == "__main__":
    main()
