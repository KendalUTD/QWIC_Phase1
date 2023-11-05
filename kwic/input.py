"""This module represents the input component of the kwic system."""

class Input(object):
    """Kendal's code for the Input module."""

    # Input initialize
    # Reads the input offered from MC and stores it somewhere
    def __init__(self, storage):
        self._storage = storage

    # Input: set_input
    # Stores the input of the lines into storage
    def set_input(self, file_address):
        print("Setting input...")
        with open(file_address, 'r') as f:
            '''read the first line as url and the rest as lines'''
            text_input_lines = f.readlines()
        self._storage.set_url(text_input_lines[0])
        text_input = text_input_lines[1]
        lines = text_input.split("$")
        for i, line in enumerate(lines, 1):
            self._storage.set_line(i, line)

#TODO: add a feature to read files from a folder rather than just one file