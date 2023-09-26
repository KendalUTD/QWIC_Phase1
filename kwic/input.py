"""This module represents the input component of the kwic system."""

from kwic.storage import LineStorage

class Input(object):
    """Kendal's code for the Input module."""

    # Input initialize
    # Reads the input offered from MC and stores it somewhere
    def __init__(self, storage):
        self._storage = storage

    # Input: set_input
    # Stores the input of the lines into storage
    def set_input(self, text_input):
        print("Setting input...")
        lines = text_input.split("$")
        for i, line in enumerate(lines):
            words = line.split()
            for j, word in enumerate(words):
                for k, char in enumerate(word):
                    # This function calls the set_char component in the Line
                    # Storage componenet
                    self._storage.set_char(i + 1, j + 1, k + 1, str(char))