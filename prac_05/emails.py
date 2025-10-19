"""
CP1404 Practical - emails
Estimate: 25 minutes
Actual: 40 minutes
"""


def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = input("Email: ")
    # print(get_name(email))
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[name] = email
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Extract name from given email"""
    things = email.split('@')
    parts = things[0].split('.')
    name = " ".join(parts).title()
    return name


main()