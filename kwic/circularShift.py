"""This module represents the Circular Shift component of the kwic system."""

class CircularShift:

    storage = None
    lines = []
    circular_shifted_lines = []

    def __init__(self, storage):
        """this acts as the setup method in the diagram"""
        self.storage = storage

    def setup(self):
        '''get the lines from storage'''

        self.lines = []

        x = 1
        line = self.storage.get_line(x)
        while line is not None:
            self.lines.append(line)
            x += 1
            line = self.storage.get_line(x)

        self.__circular_shift()


    def __circular_shift(self):
        '''shifts every word in every line '''

        for line in self.lines:
            words = line.split()
            temp_words = words
            for _ in range(len(words)):
                
                temp_words = [temp_words[-1]] + temp_words[:-1]
                shifted_line = ' '.join(temp_words)
                self.circular_shifted_lines.append(shifted_line)


    def get_shifted_lines(self):
        return self.circular_shifted_lines