"""
CP1404 Practical
Unreliable Car
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of Car that drives based on reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive car depending on reliability."""
        random_number = randint(0, 100)

        if random_number > self.reliability:
            return super().drive(distance)
        else:
            return 0

