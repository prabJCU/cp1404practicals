"""
CP1404 Practical
Unreliable Car Test
"""

from prac_09.unreliable_car import UnreliableCar

car = UnreliableCar("Car Test", 100, 30)

for i in range(10):
    distance_driven = car.drive(10)
    print(f"Attempt {i+1}: Drove {distance_driven}km | Fuel: {car.fuel}")