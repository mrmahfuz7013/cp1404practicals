"""
CP1404/CP5632 Practical - Files
Make the appropriate choice of file-reading technique for each of these questions:
- read()
- readline()
- readlines()
- for line in file
"""

# 1. Ask user for their name and write it to name.txt
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2. Read the name back from name.txt and greet
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. Read all numbers from numbers.txt and print the total
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
