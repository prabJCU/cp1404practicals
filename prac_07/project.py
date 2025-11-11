"""
CP1404 Practical - Project class
Estimate: 25 minutes
Actual: 20 minutes
"""

class Project:
    """Represent a project with name, start date, priority, cost, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, " \
               f"completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare projects by priority (lower the number, higher the priority)"""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == 100
