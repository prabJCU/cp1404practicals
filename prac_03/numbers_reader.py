"""
CP1404 - Files practical
"""


name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# read first two numbers in .txt and add them
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())

total = first_number + second_number
print(f"The total of the first two numbers is: {total}")

# read all numbers in .txt and total them
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)

print(f"The total of all numbers is: {total}")
