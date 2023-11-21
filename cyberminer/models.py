"""Placeholder module for backend processing."""

from enum import Enum

URLS = [
    "https://www.facebook.com",
    "https://www.google.com",
    "https://www.instagram.com"
]

DB_ENTRIES = [
    "here is some random text",
    "here we go",
    "here is another",
    "there is another way",
    "there we go again",
    "here, there, everywhere"
]

class SortMethod(Enum):
    ALPHABETICALLY = "some_value"
    FIXME1 = "fixme"
    FIXME2 = "fixme"

def search(query, sort_method):
    """Search the database.
    
    Parameters:
        query (str): the search bar text after clicking the search button
        sort_method (SortMethod): the requested method for sorting the results

    Returns:
        List of URLs.
    """
    return URLS

def do_autocompletion(text):
    """Perform the autocompletion.
    
    Parameters:
        text (str): the latest string entered into the search bar

    Returns:
        List of search suggestions.
    """
    return [x for x in DB_ENTRIES if x[0:len(text)] == text]