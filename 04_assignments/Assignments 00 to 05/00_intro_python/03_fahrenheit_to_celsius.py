def main():
    # Asking user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Converting Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Printing the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Calling main function
if __name__ == '__main__':
    main()
