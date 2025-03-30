"""Each input is added to the list using append().

If the user enters an empty string (presses Enter without input), the loop breaks.

The final list is printed."""



def main():
    values = []  # Initialize an empty list

    while True:
        user_input = input("Enter a value: ")  # Ask user for input
        if user_input == "":  # If input is empty (user presses Enter)
            break  # Exit the loop
        values.append(user_input)  # Add the value to the list

    print("Here's the list:", values)  # Print the final list

if __name__ == '__main__':
    main()
