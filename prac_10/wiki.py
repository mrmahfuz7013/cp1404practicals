"""
CP1404 Practical 10 - Wikipedia API
Prompt the user for page titles and display information using the Wikipedia API.
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """Prompt for Wikipedia page titles and display title, summary, and URL."""
    title = input("Enter page title: ")

    while title != "":
        try:
            # Use auto_suggest (with underscore) for this version of the library
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(wikipedia.summary(title, sentences=3, auto_suggest=False))
            print(page.url)

        except DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)

        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        # You can keep entering new titles until you press Enter on a blank line
        title = input("\nEnter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    main()
