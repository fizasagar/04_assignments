def main():
    # Asking the user for the lengths of the three sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculating the perimeter
    perimeter = side1 + side2 + side3

    # Printing the result
    print(f"The perimeter of the triangle is {perimeter}")

# Calling main function
if __name__ == '__main__':
    main()
