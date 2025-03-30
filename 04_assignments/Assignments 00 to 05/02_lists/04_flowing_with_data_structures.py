def add_three_copies(lst, data):
    """Adds three copies of data to the list."""
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Get user input
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Display list before modification
    print("List before:", my_list)

    # Call the function to modify the list
    add_three_copies(my_list, message)

    # Display list after modification
    print("List after:", my_list)

if __name__ == '__main__':
    main()
