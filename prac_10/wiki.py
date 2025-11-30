"""
CP1404 Practical
Wikipedia API Demo
"""

import wikipedia


def main():
    """Loop asking the user for a Wikipedia page title, handling exceptions."""
    title = input("Enter page title: ")

    while title != "":
        try:
            # Get the page
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        except Exception as e:
            # Just in case something unexpected occurs
            print(f"An unexpected error occurred: {e}")

        title = input("\nEnter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    main()
