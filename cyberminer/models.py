"""Placeholder module for backend processing."""

from enum import Enum
from math import ceil
from cyberminer.engine import SearchEngine

class SortMethod(Enum):
    ALPHABETICALLY = "some_value"

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
    print("DEBUG - Doing search...")
    eng = SearchEngine()
    eng.search(query)
    results = eng.process_event()

    nresults = len(results)
    npages = ceil(nresults / nperpage)
    temp = (page - 1) * nperpage
    url_results = [x[0] for x in results]

    print("DEBUG - nresults = %d, npages = %d" % (nresults, npages))
    return nresults, npages, url_results[temp:temp + nperpage]

def do_autocompletion(text):
    """Perform the autocompletion.
    
    Parameters:
        text (str): the latest string entered into the search bar

    Returns:
        List of search suggestions.
    """
    print("DEBUG - Doing autocompletion...")
    eng = SearchEngine()
    eng.search(text)
    results = eng.perform_autocomplete(text)
    return [x[1] for x in results]