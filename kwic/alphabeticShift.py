"""This module represents the alphabetic shift component of the kwic system."""

class AlphabeticShift:
    def __init__(self, circular_shifter):
        self.circular_shifter = circular_shifter
        self.sorted_shifted_lines = []

    def alpha(self):
        '''Sorts the circularly shifted lines alphabetically using merge sort'''
        self.sorted_shifted_lines = self.merge_sort(self.circular_shifter.get_shifted_lines())

    def merge_sort(self, lines):
        if len(lines) <= 1:
            return lines

        # Split the list in half
        mid = len(lines) // 2
        left_half = lines[:mid]
        right_half = lines[mid:]

        # Recursively merge sort both halves
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        # Merge the sorted halves
        sorted_lines = []
        left_index, right_index = 0, 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
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
