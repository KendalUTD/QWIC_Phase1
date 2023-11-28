"""This module represents the master control component of the kwic system."""

from kwic.input import Input
from kwic.storage import LineStorage
from kwic.circularShift import CircularShift
from kwic.alphabeticShift import AlphabeticShift
from kwic.output import Output

import sqlite3

conn = sqlite3.connect('kwic.db')
cursor = conn.cursor()

# check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kwic'")
if cursor.fetchone() is None:
    # create the table
    cursor.execute("CREATE TABLE kwic (url text, line text)")
    conn.commit()
conn.close()

conn = sqlite3.connect('kwicOrg.db')
cursor = conn.cursor()
#check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kwic'")
if cursor.fetchone() is None:
    # create the table
    cursor.execute("CREATE TABLE kwic (url text, line text)")
    conn.commit()
conn.close()


class Controller(object):
    """Orchestrates the KWIC processing."""
    def __init__(self):
        # Create single instances for each stage, passing a reference to its neighboring stage
        self._storage = LineStorage()
        self._input = Input(self._storage)
        self._circular_shifter = CircularShift(self._storage)
        self._alpha_shifter = AlphabeticShift(self._circular_shifter, self._storage)
        self._output = Output(self._circular_shifter, self._alpha_shifter)

    def run(self):
        """Entry point into KWIC processing."""
        # text_input = "Something from the input mechanism$Here is some more lines$Did you know that cashews come from a fruit$Spider-Man does whatever he can$Software Engineering is kinda fun maybe I don't know"
        # text_input = input("Enter lines (separate lines with $): ")
        # print("Text Input:\n" + text_input)
        self._input.set_input(file_address="kwic/14.txt")
        self._circular_shifter.setup()
        self._alpha_shifter.setup()
        self._output.setup()