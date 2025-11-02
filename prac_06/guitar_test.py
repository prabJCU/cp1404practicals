"""
CP1404 Practical - Guitar Test
Manual testing for Guitar Class
Estimate: 5 minutes
Actual: 5 minutes
"""

from prac_06.guitar import Guitar

g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
g2 = Guitar("Another Guitar", 1988, 23653.59)

print(f"{g1.name} get_age(): Expected {103}. Got {g1.get_age()}")
print(f"{g2.name} get_age(): Expected {37}. Got {g2.get_age()}")
print()
print(f"{g1.name} is_vintage(): Expected {True}. Got {g1.is_vintage()}")
print(f"{g2.name} is_vintage(): Expected {False}. Got {g2.is_vintage()}")