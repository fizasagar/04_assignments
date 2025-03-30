def get_first_element(lst):
    """Prints the first element of the given list."""
    print("The first element is:", lst[0])  # Access and print the first element

def main():
    # Ask the user how many elements they want to enter
    n = int(input("Enter the number of elements in the list: "))

    # Initialize an empty list
    my_list = []

    # Collect user input for each element
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    # Call the function to print the first element
    get_first_element(my_list)

if __name__ == '__main__':
    main()
