"""This module represents the line storage component of the kwic system."""

class LineStorage(object):
    """Placeholder for the Line Storage module."""
    def __init__(self):
        self._lines = dict()

    def set_char(self, l, w, c, d):
        """Causes the c-th character in the w-th word of the l-th line to be d."""
        if l <= 0 or w <= 0 or c <= 0:
            return 
        
        line = self._lines.get(l)
        if line is None:
            self._lines[l] = {
                w: {
                    c: d
                }
            }
        else:
            word = line.get(w)
            if word is None:
                self._lines[l][w] = {
                    c: d
                }
            else:
                self._lines[l][w][c] = d


    def char(self, l, w, c):
        """Returns c-th character in the w-th word of the l-th line. Returns None if out-of-range."""
        try:
            return self._lines[l][w][c]
        except KeyError as e:
            return None

    def word(self, l):
        """Returns the number of words in line l."""
        try:
            return len(self._lines[l])
        except KeyError as e:
            return 0