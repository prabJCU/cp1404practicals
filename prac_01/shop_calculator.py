"""
CP1404 - Practical 1
Shop Calculator
"""

DISCOUNT = 0.1

items_amount = int(input("Number of items: "))
total_price = 0
while items_amount < 0:
    print("Invalid number of items!")
    items_amount = int(input("Number of items: "))
else:
    for i in range(items_amount):
        item_price = float(input("Price of item: "))
        total_price = item_price + total_price

if total_price > 100:
    total_price = total_price - (DISCOUNT * total_price)

print(f"Total price for {items_amount} items is ${total_price:.2f}")