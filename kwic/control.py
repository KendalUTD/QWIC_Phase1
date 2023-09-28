"""This module represents the master control component of the kwic system."""

from kwic.input import Input
from kwic.storage import LineStorage
from kwic.circularShift import CircularShift
from kwic.alphabeticShift import AlphabeticShift
from kwic.output import Output


class Controller(object):
    """Orchestrates the KWIC processing."""
    def __init__(self):
        # Create single instances for each stage, passing a reference to its neighboring stage
        self._storage = LineStorage()
        self._input = Input(self._storage)
        self._circular_shifter = CircularShift(self._storage)
        self._alpha_shifter = AlphabeticShift(self._circular_shifter)
        self._output = Output(self._alpha_shifter)

    def run(self):
        """Entry point into KWIC processing."""
        self._input.set_input("Something from the input mechanism$Here is some more")
        self._circular_shifter.setup()
        self._alpha_shifter.alpha()
        self._output.get_output()