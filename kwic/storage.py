"""This module represents the line storage component of the kwic system."""

class LineStorage(object):
    def __init__(self):
        self._lines = dict()

    def set_line(self, l, d):
        """Causes the l-th line to be d."""
        if l <= 0:
            return 
        self._lines[l] = d

    def get_line(self, l):
        """Returns l-th line. Returns None if out-of-range."""
        try:
            return self._lines[l]
        except KeyError as e:
            return None

    def word(self, l):
        """Returns the number of words in line l."""
        try:
            return len(self._lines[l].split())
        except KeyError as e:
            return 0