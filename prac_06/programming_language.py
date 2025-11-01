"""
CP1404 Practical - ProgrammingLanguage class
Estimate: 30 mins
Actual: 28 mins
"""


class ProgrammingLanguage:
    """Represent a programming language with typing style, reflection support, and first appearance year."""

    def __init__(self, name, typing, reflection, year):
        """
        Initialise a ProgrammingLanguage instance.

        name: str - language name (e.g. "Python")
        typing: str - "Dynamic" or "Static"
        reflection: bool - True if it supports reflection
        year: int - first appeared year
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """
        Return True if the language is dynamically typed.
        """
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """
        Return a string representation of the ProgrammingLanguage.
        Example: Python, Dynamic Typing, Reflection=True, First appeared in 1991
        """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
