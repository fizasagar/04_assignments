# Speed of light constant (meters per second)
C = 299792458  

def main():
    # User se mass input lena
    mass = float(input("Enter kilos of mass: "))

    # Einstein's equation apply karna
    energy = mass * (C ** 2)

    # Output show karna
    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s\n")
    print(f"{energy} joules of energy!")

# Function ko run karna
if __name__ == "__main__":
    main()
