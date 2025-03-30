def get_last_element(lst):
    """Prints the last element of the given list."""
    print("The last element is:", lst[-1])  # Access and print the last element

def main():
    # Ask the user how many elements they want to enter
    n = int(input("Enter the number of elements in the list: "))

    # Initialize an empty list
    my_list = []

    # Collect user input for each element
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    # Call the function to print the last element
    get_last_element(my_list)

if __name__ == '__main__':
    main()
