"""
      Joel Coddington-Lopez
      Boston University - Summer 2025
      This script tests the MusicAPI class.
"""
import os
from MusicAPI import MusicAPI

def empty_session_test():
    """Unit test for checking if a session with no queries works as expected"""
    print("empty")
    return True

def valid_session_test():
    """Unit test for checking if a session with one query works as expected"""
    print("valid")
    return True

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