"""
CP1404 Practical
Lists Warm-up
This program explores basic list indexing, slicing, and membership operations.
"""

# Original list
numbers = [3, 1, 4, 1, 5, 9, 2]

# ------------------------------
# Part 1: Predict the output of each expression
# (Write your predicted answers as comments before testing in the console)

# numbers[0]        -> 3
# numbers[-1]       -> 2
# numbers[3]        -> 1
# numbers[:-1]      -> [3, 1, 4, 1, 5, 9]
# numbers[3:4]      -> [1]
# 5 in numbers      -> True
# 7 in numbers      -> False
# "3" in numbers    -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# ------------------------------
# Part 2: Perform the following modifications and checks

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all elements from numbers except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
