"""
      Joel Coddington-Lopez
      Boston University - Summer 2025
      This class initializes the iTunes API for use in `main.py`.
"""
import requests

class MusicAPI:
    def __init__(self, session_name):
        """Constructor sets up class variables and local session info"""
        self.ENDPOINT = "https://itunes.apple.com/search?"
        self.SEARCH_PARAMS = {
            "entity": ["music", "song"],
            "limit": 100
        }
        self.__session = session_name
        self.__session_logs = []

    def __str__(self):
        """Overload printing of class instantiation to read filename"""
        return self.__session + ".txt"

    def __del__(self):
        """Overload destructor to print result log location"""
        print("-----------------------------------")
        print("> Query engine has now shut down.")
        print("> Result logs are available in", self)

    def query(self, term):
        """Queries the iTunes API and returns raw API response"""
        print("> Loading... this may take a moment!")
        try:
            # construct request URL
            req_url = (self.ENDPOINT + "limit={l}&"
                       .format(l=self.SEARCH_PARAMS['limit']))
            for entity in self.SEARCH_PARAMS["entity"]:
                req_url += "entity={e}&".format(e=entity)

            # format search term and insert into request URL
            term_list = term.split(" ")
            term_string = "+".join(term_list)
            req_url += "term={term_string}".format(term_string=term_string)

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
        dataset_size = len(genre_list)

        # occasionally, the iTunes API ignores `LIMIT` (likely a bug?) and
        # still returns a dataset with length > 100, so we'll chop that
        # excess data off in the event this edge case occurs
        if dataset_size > 100:
            genre_list = genre_list[0 : 100]
            dataset_size = 100

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
            "Out of {size} result(s) for {term}, {x} genre(s) were identified."
            .format(
                size=dataset_size, term=term, x=len(present_genres)
            ),
            "Here are the stats:",
        ]

        # derive percentages from genre_stats, need to set value of each
        # stats_by_genre item to the percentage rather than count
        for key, value in stats_by_genre.items():
            stats_by_genre[key] = round(
                stats_by_genre[key] / dataset_size * 100)
            stats_by_genre[key] = int("{:.0f}".format(stats_by_genre[key]))

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