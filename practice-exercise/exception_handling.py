# Task 1 -  Safe divider
"""
- Write a function called safe_divide(a, b) that:
- Takes two numbers.
- Returns the result of a / b.
- Handles the case where b is zero and prints "Cannot divide by zero".
"""
def safe_divide(a, b):
    
    if b == 0:      # Check if divisor is zero
        raise ZeroDivisionError("Error: cannot divide by zero.")    # Raise error for division by zero
    return a / b    # Perform safe division

result = safe_divide(10, 2)     # Call the function and pass arguments
print(result)       

# Task 2
"""
You have a dictionary:
students = {"Uche": 25, "Zara": 22}
Write a function that asks for a student's name and prints their age.
Use exception handling to deal with the case when the name is not found.
"""

students = {"Uche": 25, "Zara": 22}

def student_age():
    # Get tudent name from user input
    try:
        name = input("Enter student name: ")
        print(f"{name} is {students[name]} years old.")     # Print student name and age
    
    except KeyError:    # Display error message to user
        print("Student not found.")

student_info = student_age()    # Call function


# Task 3
"""
Type Checker
Write a function that takes two inputs and adds them together.
If either input is not a number, catch the error and print "Only numbers are allowed".
"""
def addition(x, y):
    # Iterate until the correct data type is entered
    while True:
        try:
            x = int(input("Enter the numbers to add: "))
            y = int(input("Enter another number to add: "))
            return x + y
        
    # Display error message
        except ValueError:
            print("Only numbers are allowed. Please enter a number: ")
    

add = addition(10, 5)
print(add)


# Task 4
"""
Create a list of 5 items.
Write a function that takes a user input and prints the item at that position.
Use exception handling to catch when the index is out of range or not a number.

"""

list01 = ["mango", "orange", "avocado", "pineapple", "almond", "grape"]

def fruits():
        try:

            # Collect user input to add to the existing list
            new_fruit = input("Add a fruit to the list: ")

            # Prompt to decide the index to position new input
            index = int(input(f"Enter the position (0 - {len(list01)-1}) to place the fruit: "))

            list01.append(new_fruit)    #  Add new fruit to end of list
            fruit = list01.pop()        # Remove last element from list
            

            list01.insert(index, fruit)  # Insert fruit at specified index
            print(list01)               # Print updated list
    
        except ValueError: 
            
            # Handle non-numeric input error
            print("Please enter a number for the position")
    
        except IndexError:
        # Handle out of range index error
            print(f"That index is out of range. Please enter a number from 0 to {len(list01)-1}.")


fruit_list = fruits()
print(fruit_list)


# Task 5
"""
File Not Found
Ask the user to input a filename, and try to open that file for reading.
If the file doesn't exist, catch the exception and print "File not found".

"""


def open_file():
        # Get filename from user input

    try:
        filename = input("Enter a file name to access file: ")

        # Attempt to open file in read mode

        with open(filename, "r") as file:
        
        # Read and print file contents
            print(file.read())
    
    # Handle file not found exception
    except FileNotFoundError:
    
    # Print error message for file not found
        print("File not found")

files = open_file()