# This script will calculate the user’s monthly savings based on inputted monthly income and expenses

# Prompt User Input for Financial Details

monthly_income = input('Enter your monthly income: ')
total_monthly_expenses = input('Enter your total monthly expenses: ')

# Calculate monthly expenses
monthly_savings = monthly_income - total_monthly_expenses

# Display the user’s monthly savings
print("Your monthly savings is", monthly_savings)


# Project Annual Savings assuming annual interest is 5%
annual_interest = 5

# Annual projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the user's projected annual savings
print("Projected savings after one year, with interest, is: ", "$",projected_savings)
