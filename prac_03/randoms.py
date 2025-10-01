"""
CP1404/CP5632 - Practical
Random numbers and questions about their ranges.
"""

import random

# Test lines from the instructions
print(random.randint(5, 20))        # line 1
# Smallest possible: 5, largest possible: 20 (inclusive)

print(random.randrange(3, 10, 2))   # line 2
# Possible values: 3, 5, 7, 9
# Smallest possible: 3, largest possible: 9
# Could it produce a 4? No.

print(random.uniform(2.5, 5.5))     # line 3
# Smallest possible ~2.5, largest possible ~5.5 (float, inclusive of ends in practice)

# Extra: random number between 1 and 100 inclusive
print(random.randint(1, 100))
