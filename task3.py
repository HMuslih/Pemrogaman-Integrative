def categorize_number():
    # Get user input for a number
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Categorize the number
    if number < 100:
        category = "Small"
    elif 100 <= number <= 200:
        category = "Medium"
    else:
        category = "Large"

    # Display the result
    print(f"The category of the number {number} is: {category}")

# Call the function to run the program
categorize_number()
