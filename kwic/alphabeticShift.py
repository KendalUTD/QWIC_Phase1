"""This module represents the alphabetic shift component of the kwic system."""

from circularShift import CircularShift

class AlphabeticShift:
    def __init__(self, circular_shifter):
        self.circular_shifter = circular_shifter
        self.sorted_shifted_lines = []

    def setup(self):
        self.csLines = self.circular_shifter.get_shifted_lines()
        self.__alpha()

    def __alpha(self):
        '''Sorts the circularly shifted lines alphabetically using merge sort'''
        self.sorted_shifted_lines = self.__merge_sort(self.csLines)

    def __merge_sort(self, lines):
        if len(lines) <= 1:
            return lines

        # Split the list in half
        mid = len(lines) // 2
        left_half = lines[:mid]
        right_half = lines[mid:]

        # Recursively merge sort both halves
        left_half = self.__merge_sort(left_half)
        right_half = self.__merge_sort(right_half)

        # Merge the sorted halves
        sorted_lines = []
        left_index, right_index = 0, 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index].lower() < right_half[right_index].lower():
                sorted_lines.append(left_half[left_index])
                left_index += 1
            else:
                sorted_lines.append(right_half[right_index])
                right_index += 1

        sorted_lines.extend(left_half[left_index:])
        sorted_lines.extend(right_half[right_index:])
        return sorted_lines

    def get_sorted_lines(self):
        return self.sorted_shifted_lines
