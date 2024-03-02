def calculate_sum():
    # Get user input for a number
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return

    # Calculate the sum of values from 1 up to the number
    total_sum = sum(range(1, number + 1))

    # Display the result
    print(f"The sum of values from 1 to {number} is: {total_sum}")

# Call the function to run the program
calculate_sum()
