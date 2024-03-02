def calculate_sum():
    total_sum = 0

    # Read numbers until -1 is entered
    while True:
        try:
            number = int(input("Enter a number (enter -1 to finish): "))
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
            continue

        # Check if the entered number is -1 to break the loop
        if number == -1:
            break

        # Add the entered number to the total sum
        total_sum += number

    # Display the result
    print(f"The sum of all entered numbers is: {total_sum}")

# Call the function to run the program
calculate_sum()
