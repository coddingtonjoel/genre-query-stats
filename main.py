"""
      Joel Coddington-Lopez
      Boston University - Summer 2025
      This script calculates genre statistics for a given search term
      using the open-source iTunes API.
"""
from MusicAPI import MusicAPI

def process_input(api, term):
    """Processes user input from menu loop and calls MusicAPI"""
    res = api.query(term)
    stats = api.derive_genre_stats(res, term)

    if len(stats) == 0:
        print("No results were found for your search term.")
    else:
        for item in stats:
            print(item)

def init_session():
    """Initialize tool and prompt user for search term"""
    print("-------------------------------------")
    print("\tgenre-query-stats")
    print("\tBy Joel Coddington-Lopez")
    print("-------------------------------------")

    while True:
        session_name = (
            input("Please enter a session name to log your results: "))
        if len(session_name) == 0 or not(session_name.isalnum()):
            print("Invalid session name. Please keep your session name to",
                  "alphanumeric characters (one word). ")
            print("---------------------------------")
        else:
            break

    api = MusicAPI(session_name)

    while True:
        print("Enter a search term, or type `quit` to exit the program.")
        term = input("> ")

        if term.lower() == 'quit':
            break

        process_input(api, term)

if __name__ == "__main__":
    init_session()