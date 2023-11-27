"""Placeholder module for backend processing."""

from enum import Enum
from math import ceil

URLS = [
    "https://www.facebook.com",
    "https://www.google.com",
    "https://www.instagram.com",
    "https://www.google2.com",
    "https://www.google3.com",
    "https://www.google4.com",
    "https://www.google5.com",
    "https://www.google6.com",
    "https://www.google7.com",
    "https://www.google8.com",
    "https://www.google9.com",
    "https://www.google10.com",
    "https://www.google11.com",
    "https://www.google12.com",
    "https://www.google13.com"
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

def search(query, sort_method, page, nperpage):
    """Search the database.
    
    Parameters:
        query (str): the search bar text after clicking the search button
        sort_method (SortMethod): the requested method for sorting the results
        page (int): the requested page number
        nperpage (int): the number of results to print per page

    Returns:
        List of URLs.
    """
    nresults = len(URLS)
    npages = ceil(nresults / nperpage)
    temp = (page - 1) * nperpage
    return len(URLS), npages, URLS[temp:temp + nperpage]

def do_autocompletion(text):
    """Perform the autocompletion.
    
    Parameters:
        text (str): the latest string entered into the search bar

    Returns:
        List of search suggestions.
    """
    return [x for x in DB_ENTRIES if x[0:len(text)] == text]