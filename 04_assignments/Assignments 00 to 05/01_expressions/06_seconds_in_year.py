def main():
    # Define constants for time conversions
    DAYS_IN_YEAR = 365  
    HOURS_IN_DAY = 24  
    MINUTES_IN_HOUR = 60  
    SECONDS_IN_MINUTE = 60  

    # Calculate total seconds in a year
    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE  

    # Print the result in a nice way
    print(f"There are {seconds_in_year} seconds in a year!")

# Run the main function
if __name__ == "__main__":
    main()
