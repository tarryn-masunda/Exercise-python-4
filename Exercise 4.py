# # Question 1: Using a for loop with a list

# # TODO: Create a list of fruits

list = ["Banana", "Apple", "Pear", "Orange"]
for fruits in list:
    

# # TODO: Use a for loop to print each fruit in the list
    print(fruits)

# #-------------------------------------------------------------------------
# # Question 2: Using a whi le loop for countdown

# # TODO: Use a while loop to create a countdown from 5 to 1
number = 5
while number <= 1:
    print(number)
    number -= 1


# #-------------------------------------------------------------------------
# # Question 3: Using a for loop with range()

# # TODO: Use a for loop to print the first 10 square numbers

for x in range(1,11):
    squared = x ** 2
    print(f"Square of {x} is: {squared}")
# #-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

import random

# TODO: Create a list of colors
colours_list = ["Red","Pink","White","Yellow","Brown","Black","Blue"]

# TODO: Use a for loop to select and print 3 random colors from the list
colour = random.sample(colours_list,3)
for x in colour:
    print(x)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:


# TODO: Import the custom module and use its functions

import math_operations

sum_result = math_operations.add(2, 5)
subtract_result = math_operations.subtract(1, 6)
multiply_result = math_operations.multiply(8, 2)
divide_result = math_operations.divide(10, 5)

# Print the results
print(f"{2} + {5} = {sum_result}")
print(f"{1} - {6} = {subtract_result}")
print(f"{8} * {2} = {multiply_result}")
print(f"{10} / {5} = {divide_result}")

# # TODO: Use a while loop to create a simple calculator

