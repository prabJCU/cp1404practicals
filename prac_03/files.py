"""
CP1404 - Practical 3 - Files
"""

name = input("Enter your name: ")
out_file = open(".txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open(".txt", "r")
name = in_file.readline().strip()
in_file.close()

print(f"Hi {name}!")