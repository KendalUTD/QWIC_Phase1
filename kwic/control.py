"""This module represents the master control component of the kwic system."""

from kwic.storage import LineStorage

class Input(object):
    """Placeholder for the Input module."""
    def __init__(self, storage):
        self._storage = storage

    def set_input(self):
        print("Setting input...")
        self._storage.set_char()

class CircularShifter(object):
    """Placeholder for the Circular Shift module."""
    def __init__(self, storage):
        self._storage = storage

    def setup(self):
        print("Setting up circular shifter...")
        self._storage.char()
        self._storage.word()

    def CS_Char(self):
        print("Getting CS char...")

    def CS_Word(self):
        print("Getting CS word...")

class AlphabeticShifter(object):
    """Placeholder for the Alphabetics shift module."""
    def __init__(self, circular_shifter):
        self._circular_shifter = circular_shifter

    def alpha(self):
        print("Alphabetizing...")
        self._circular_shifter.CS_Char()
        self._circular_shifter.CS_Word()

    def ith_line(self):
        print("Getting ith line...")

class Output(object):
    """Placeholder for the Output module."""
    def __init__(self, shifter):
        self._shifter = shifter

    def get_output(self):
        print("Getting output...")
        self._shifter.ith_line()

class Controller(object):
    """Orchestrates the KWIC processing."""
    def __init__(self):
        # Create single instances for each stage, passing a reference to its neighboring stage
        self._storage = LineStorage()
        self._input = Input(self._storage)
        self._circular_shifter = CircularShifter(self._storage)
        self._alpha_shifter = AlphabeticShifter(self._circular_shifter)
        self._output = Output(self._alpha_shifter)

    def run(self):
        """Entry point into KWIC processing."""
        self._input.set_input()
        self._circular_shifter.setup()
        self._alpha_shifter.alpha()
        self._output.get_output()