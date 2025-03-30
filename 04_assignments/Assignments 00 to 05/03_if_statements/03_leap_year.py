def is_leap_year(year):
    # Check the leap year conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Enter a year: "))  # Get the year from the user

    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Run the program
main()
