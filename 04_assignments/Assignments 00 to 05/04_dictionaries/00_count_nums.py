def count_numbers():
    number_counts = {}

    while True:
        num = input("Enter a number (or press Enter to finish): ")
        if num == "":  # Stop if the user presses Enter without a number
            break
        num = int(num)  # Convert input to integer

        # Update count in the dictionary
        if num in number_counts:
            number_counts[num] += 1
        else:
            number_counts[num] = 1

    # Print results
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

count_numbers()
