"""
CP1404 Practical - Client code to use the ProgrammingLanguage class
Estimate: 15 mins
Actual: 17 mins
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create and test ProgrammingLanguage objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print them all (calls __str__)
    print(python)
    print(ruby)
    print(visual_basic)

    # Store them in a list
    languages = [python, ruby, visual_basic]

    # Print only dynamically typed ones
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
