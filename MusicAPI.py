"""
      Joel Coddington-Lopez
      Boston University - Summer 2025
      This class initializes the iTunes API for use in `main.py`.
"""
import requests

class MusicAPI:
    def __init__(self, session_name):
        self.endpoint = "https://itunes.apple.com/search?"
        self.searchParams = {
            "entity": ["music", "song"],
            "limit": 100
        }
        self.__session = session_name
        self.__session_logs = []

    def __str__(self):
        return self.__session + ".txt"

    def __del__(self):
        print("-----------------------------------")
        print("> Query engine has now shut down.")
        print("> Result logs are available in", self)

    def query(self, term):
        """Queries the iTunes API and returns raw API response"""
        try:
            # construct request URL
            req_url = (self.endpoint + "limit={l}&"
                       .format(l=self.searchParams['limit']))
            for entity in self.searchParams["entity"]:
                req_url += "entity={e}&".format(e=entity)

            # format search term and insert into request URL
            term_list = term.split(" ")
            term_string = "+".join(term_list)
            req_url += "term={term_string}".format(term_string=term_string)

            # query api
            res = requests.get(req_url)


            # raise exception it status code is not correct
            if not res.status_code == 200:
                raise Exception
            return res.json()
        except:
            print("An error occurred when communicating with the API.")
            return None

    def derive_genre_stats(self, data, term):
        """Converts raw API response into human-readable statistics.
        Returns a list of summarized genre data from the search results."""

        # parse data from JSON object
        results = data['results']
        genre_list = [e["primaryGenreName"] for e in results]

        # use a set to calculate total amount of individual genres returned
        present_genres = set(genre_list)

        # tally up the popularity of each present genre
        stats_by_genre = dict()
        for item in genre_list:
            if item in stats_by_genre.keys():
                stats_by_genre[item] += 1
            else:
                stats_by_genre[item] = 1

        genre_stats = [
            "Out of 100 results for {term}, {x} genres were identified.".format(
                term=term, x=len(present_genres)
            ),
            "Here are the stats:",
        ]

        # add stat data to genre_stats based on percentage in descending order
        for i in range (100, 0, -1):
            for key, value in stats_by_genre.items():
                if i == value:
                    genre_stats.append("\t- {x}% - {g}".format(x=value, g=key))


        # self.__write_log(genre_stats)
        return tuple(genre_stats)

    def __write_log(self):
        """Writes statistics from session into a local text file"""
        print(self.__session)