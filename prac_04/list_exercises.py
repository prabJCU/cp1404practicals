"""
CP1404 - Practical
List Exercises
"""
NUMBER_AMOUNT = 5

numbers = []
for i in range(NUMBER_AMOUNT):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is: {numbers[0]}"
      f"\nThe last number is: {numbers[-1]}"
      f"\nThe smallest number is: {min(numbers)}"
      f"\nThe largest number is: {max(numbers)}"
      f"\nThe average number is: {sum(numbers)/len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print(f"Access Granted")
else:
    print(f"Access Denied")