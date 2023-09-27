"""This module represents the input component of the kwic system."""

from kwic.storage import LineStorage

class Input(object):
    """Kendal's code for the Input module."""

    # Input initialize
    # Reads the input offered from MC and stores it somewhere
    def __init__(self, storage):
        self._storage = storage

    def __readFile(filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                f.close()
            return content
        except FileNotFoundError:
            raise Exception('Function not yet implemented!')

    # Input: set_input
    # Stores the input of the lines into storage
    # Assumes the first Character in a line is not " "
    def set_input(self, text_input):
        text = self.__readFile(text_input)
        print("Setting input...")
        lines = text.split("$")
        for i, line in enumerate(lines):
            # This function calls the set_char component in the Line
            # Storage componenet
            self._storage.set_line(line)