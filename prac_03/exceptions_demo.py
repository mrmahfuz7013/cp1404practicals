"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - If the user enters something that cannot be converted to an int (e.g. letters or symbols).
2. When will a ZeroDivisionError occur?
   - If the user enters 0 for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by checking that the denominator is not zero before dividing.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # avoid ZeroDivisionError by checking denominator
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
