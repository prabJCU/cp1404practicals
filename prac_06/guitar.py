"""
CP1404 Practical - Guitar.
Estimate: 15 minutes
Actual: 13 minutes
"""
CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Guitar class that stores details regarding a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """Return the age of the Guitar based on the current year."""
        guitar_age = CURRENT_YEAR - self.year
        return guitar_age

    def is_vintage(self):
        """Determine if guitar is vintage based on its age"""
        return self.get_age() >= VINTAGE_AGE