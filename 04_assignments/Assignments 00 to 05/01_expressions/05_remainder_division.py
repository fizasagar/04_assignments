def main():
    # User se pehla number lena
    num1 = int(input("Please enter an integer to be divided: "))
    
    # User se doosra number lena
    num2 = int(input("Please enter an integer to divide by: "))

    # Division ka result calculate karna
    quotient = num1 // num2
    remainder = num1 % num2

    # Output show karna
    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

# Function ko run karna
if __name__ == "__main__":
    main()
