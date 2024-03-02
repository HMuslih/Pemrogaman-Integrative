def divide_by_three():
    # Get user input for a whole number
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return

    # Calculate the result and display with three decimal places
    result = round(number / 3, 3)

    # Display the result
    print(f"The result of dividing {number} by 3 is: {result}")

# Call the function to run the program
divide_by_three()
