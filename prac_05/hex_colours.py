"""
CP1404 Practical
Hex Colours
"""

HEX_COLOURS = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "acid blue": "#c0c0c0",
               "army green": "#4b5320", "ash grey": "#b2beb5", "bright maroon": "#c32148",
               "navy blue": "#1974d2", "brown": "#a52a2a", "camel": "#c19a6b", "candy apple red": "#ff0800"}

colour_name = input("Enter Colour Name: ").lower()

while colour_name != "":
    try:
        print("The Hex Code for", colour_name.title(), "is,", HEX_COLOURS[colour_name])
    except KeyError:
        print("Invalid Colour name.")
    colour_name = input("Enter colour name: ").lower()
