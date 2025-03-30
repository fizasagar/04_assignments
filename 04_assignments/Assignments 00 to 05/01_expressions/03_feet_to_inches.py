# Constant: 1 foot = 12 inches
INCHES_IN_FOOT = 12  

def main():
    # User se feet ka input lena
    feet = float(input("Enter number of feet: "))

    # Feet ko inches me convert karna
    inches = feet * INCHES_IN_FOOT

    # Output show karna
    print(f"That is {inches} inches!")

# Function ko run karna
if __name__ == "__main__":
    main()
