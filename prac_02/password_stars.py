def main():
    get_password()

def get_password():
    password = input("Enter password: ")
    print_password(password)

def print_password(password):
    for i in range(0, len(password)):
        print("*", end="")


main()