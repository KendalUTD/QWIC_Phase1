"""Placeholder for handling requests."""

from enum import Enum

class SortMethod(Enum):
    ALPHABETICALLY = "some_value"
    FIXME1 = "fixme"
    FIXME2 = "fixme"

def submit_request(query, sort_method):
    return [
        "https://www.facebook.com",
        "https://www.google.com",
        "https://www.instagram.com"
    ]