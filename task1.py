import math

def calculate_monthly_salary():
    # Get user input for salary
    try:
        salary = float(input("Enter your annual salary: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Calculate monthly salary
    monthly_salary = math.ceil(salary / 12)

    # Display the result
    print(f"Your monthly salary is: {monthly_salary}")

# Call the function to run the program
calculate_monthly_salary()
