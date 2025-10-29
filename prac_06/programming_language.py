"""
CP1404 - Programming Language
Estimate: 15 minutes
Actual: 20 minutes
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        self.language = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a programming language."""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed"""
        return self.typing.lower() == "dynamic"
