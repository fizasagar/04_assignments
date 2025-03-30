MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH"""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last element
        print("Removed:", removed_item)  # Print the removed item

def main():
    user_list = []  # Initialize an empty list

    # Get user input for the list
    while True:
        user_input = input("Enter a value (or press Enter to stop): ")
        if user_input == "":
            break  # Stop taking input if the user presses Enter
        user_list.append(user_input)  # Add input to the list

    print("Original list:", user_list)
    shorten(user_list)  # Call the shorten function
    print("Final list:", user_list)  # Print the final modified list

if __name__ == '__main__':
    main()
