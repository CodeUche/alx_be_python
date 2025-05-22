# This scrips is a User Input Age Calculator

# Prompt the user to input their current age with the question

# Assign the variables for the years and future age

age = int(input("How old are you: "))

current_year = 2023
target_year = 2050

years_to_add = target_year - current_year
future_age = age + years_to_add

# Print the output of the user's future age

print ("In 2050 you will be", future_age, "years old.")
