"""
CP1404 Practical
Unreliable Car
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """..."""

    def __init__(self, name, fuel, reliability=0.0):
        """..."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def generate_random_number(self):
        """..."""
        random_number = randint(0, 100)
        return random_number

    def drive(self, distance):
        """..."""


