"""This module represents the output component of the kwic system."""

import random

ENDC = '\033[0m'

COLORS = list()
COLORS.append('\033[31m')
COLORS.append('\033[32m')
COLORS.append('\033[33m')
COLORS.append('\033[34m')
COLORS.append('\033[35m')
COLORS.append('\033[36m')
COLORS.append('\033[37m')

class Output(object):
    def __init__(self, shifter):
        self._shifter = shifter

    def _print_line(self, line):
        x = random.randint(0,6)
        print(COLORS[x] + line + ENDC)

    def get_output(self):
        print("Getting output...")
        print("\n")
        for line in self._shifter.get_sorted_lines():
            self._print_line(line)