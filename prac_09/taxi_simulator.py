"""
CP1404 Practical
Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Set up taxis and start the simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    run_simulator(taxis)


def run_simulator(taxis):
    """
    Run the main simulation loop for choosing and driving taxis.
    """
    print("Let's drive!")

    bill_to_date = 0.0
    current_taxi = None

    choice = get_menu_choice()

    while choice != "q":

        if choice == "c":
            current_taxi = choose_taxi(taxis)

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                bill_to_date += trip_cost
                print(f"Your {current_taxi._name} trip cost you ${trip_cost:.2f}")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        choice = get_menu_choice()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_menu_choice():
    """Display menu and return the user's menu selection."""
    print(MENU)
    return input(">>> ").lower()


def choose_taxi(taxis):
    """
    Display taxis and allow user to select one.
    """
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
    except ValueError:
        pass

    print("Invalid taxi choice")
    return None


def drive_taxi(taxi):
    """
    Ask for distance and return the fare for the trip.
    """
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


if __name__ == "__main__":
    main()
