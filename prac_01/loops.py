"""
CP1404 - Practical 1
Loops
"""

# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
star_amount = int(input('Number of stars: '))
for i in range(star_amount):
    print("*", end='')
print()

# d
line_amount = int(input('Number of lines: '))
for i in range(1, line_amount + 1):
    print("*" * i)