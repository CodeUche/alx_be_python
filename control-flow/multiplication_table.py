# A multiplication table for any chosen number
# This demonstrate the possibilities with for loop iterations

# Prompt user to choose a number
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11)
    
    # Inner loop to iterate through columns
    total = number * i

    print(f"{number} * {i} = {total}", end = " ")
    print() # Move to a new line after each rows

