"""
      Joel Coddington-Lopez
      Boston University - Summer 2025
      This script tests the MusicAPI class.
"""
import os
from MusicAPI import MusicAPI

def empty_session_test():
    """Unit test for checking if a session with no queries works as expected"""
    api = MusicAPI("empty_session_test", test_mode=True)
    api.write_logs()

    cwd = os.getcwd()
    path = os.path.join(cwd, "empty_session_test.txt")

    # assert the file doesn't exist, because no query was run
    try:
        assert os.path.exists(path) == False
        return True
    except AssertionError:
        return False

def valid_session_test():
    """Unit test for checking if a session with one query works as expected"""
    api = MusicAPI("valid_session_test", test_mode=True)
    search_term = "song"
    res = api.query(search_term)
    api.derive_genre_stats(res, search_term)
    api.write_logs()

    cwd = os.getcwd()
    path = os.path.join(cwd, "valid_session_test.txt")

    # check that file is the right length and contains the search term
    try:
        file = open(path, "r")
        lines = file.readlines()
        assert len(lines) == 13
        assert "Out of 100 result(s) for song" in lines[0]

        # delete the test file
        os.remove(path)
        return True
    except AssertionError:
        os.remove(path)
        return False
    except FileNotFoundError:
        return False



# unit test aggregate to run in main
unit_tests = [
    empty_session_test,
    valid_session_test,
]

if __name__ == "__main__":
    """Runs all unit tests"""
    test_results = dict()

    # run each test and add test result to dict
    for test in unit_tests:
        res = test()
        test_results[test.__name__] = res

    # print test results
    print("Unit tests for MusicAPI class:")
    print("------------------------------")
    for key, value in test_results.items():
        print(key + ": ", end="")
        if value:
            print("Success")
        else:
            print("Failed")