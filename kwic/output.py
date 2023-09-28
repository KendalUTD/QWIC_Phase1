"""This module represents the output component of the kwic system."""

import random
import time

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
    def __init__(self, circle_shifter, alpha_shifter):
        self.circle_shifter = circle_shifter
        self.alpha_shifter = alpha_shifter
        self.color_mover = 0
        self.line_dict = {}

    def _print_line(self, line):
        line_mod = str(sorted(line.split()))

        # Assign a line a color if line does not have one
        if str(line_mod) not in self.line_dict:
            self.line_dict[line_mod] = COLORS[self.color_mover]
            self.color_mover += 1
        
        # x = random.randint(0,len(COLORS)-1)

        # print line with respective color
        print(self.line_dict[line_mod] + line + ENDC)

    def _has_noise_word(self, line):
        word = line.split()[0].lower()
        if len(word) <= 2:
            return True
        elif word in NOISE_WORDS:
            return True
        return False

    def get_output(self):
        print("\nGetting CS Lines\n")
        for line in self.circle_shifter.get_shifted_lines():
            self._print_line(line)
        time.sleep(5)
        print("\nGetting output...")
        print("\n")
        for line in self.alpha_shifter.get_sorted_lines():
            if self._has_noise_word(line):
                continue
            self._print_line(line)