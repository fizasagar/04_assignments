# Dictionary with fruit names and their prices
fruit_prices = {
    "apple": 5.0,
    "durian": 15.0,
    "jackfruit": 10.0,
    "kiwi": 3.5,
    "rambutan": 7.0,
    "mango": 8.5
}

total_cost = 0  # Variable to store total price

# Loop through the dictionary to ask user input
for fruit, price in fruit_prices.items():
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    total_cost += quantity * price  # Calculate total price

# Print total cost
print(f"\nYour total is ${total_cost:.2f}")
