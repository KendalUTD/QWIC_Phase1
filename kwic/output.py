"""This module represents the output component of the kwic system."""

import sqlite3
import random
import time

conn = sqlite3.connect('kwic.db')
cursor = conn.cursor()

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

    def setup(self):
        self.get_output()
        self._save_to_dB()

    def _print_line(self, line):
        line_mod = str(sorted(line.split()))

        # Assign a line a color if line does not have one
        if str(line_mod) not in self.line_dict:
            self.line_dict[line_mod] = COLORS[self.color_mover]
            self.color_mover += 1
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
        for line in self.circle_shifter.get_lines():
            self._print_line(line)
        # time.sleep(5)
        print("\nGetting output...")
        print("\n")
        for line in self.alpha_shifter.get_lines():
            if self._has_noise_word(line[1]):
                continue
            self._print_line(line[1])

    def _save_to_dB(self):
        '''save the sorted list of shifted lines to db'''
        for line in self.alpha_shifter.get_lines():
            if not self._has_noise_word(line[1]):
                cursor.execute("INSERT INTO kwic VALUES (?, ?)", (line[0], line[1]))
        conn.commit()
        conn.close()
