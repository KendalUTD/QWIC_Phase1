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

NOISE_WORDS = ['with', 'then', 'they', 'the', 'and', 'or', 'you', 'from']

class Output(object):
    def __init__(self, shifter):
        self._shifter = shifter

    def _print_line(self, line):
        x = random.randint(0,len(COLORS)-1)
        print(COLORS[x] + line + ENDC)

    def _has_noise_word(self, line):
        word = line.split()[0].lower()
        if len(word) <= 2:
            return True
        elif word in NOISE_WORDS:
            return True
        return False

    def get_output(self):
        print("Getting output...")
        print("\n")
        for line in self._shifter.get_sorted_lines():
            if self._has_noise_word(line):
                continue
            self._print_line(line)