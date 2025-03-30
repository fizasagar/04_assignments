import math 

def main():
    # User se perpendicular sides ka input lena
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Pythagorean theorem apply karna
    bc = math.sqrt(ab**2 + ac**2)

    # Output show karna
    print(f"\nThe length of BC (the hypotenuse) is: {bc}")

# Function ko run karna
if __name__ == "__main__":
    main()
