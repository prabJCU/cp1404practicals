"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode:

get sales
if sales < $1,000:
    bonus = 10%
else
    bonus = 15%
______________________________________________________________________
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = 0.1
    else:
        bonus = 0.15
    user_bonus = sales * bonus
    print(f"${user_bonus}")
    sales = float(input("Enter sales: $"))








