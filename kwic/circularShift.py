

class CircularShift:

    lines = []
    circular_shifted_lines = []

    def __init__(self, storage):
        """this acts as the setup method in the diagram"""

        self.setup(storage)
        self.__circular_shift()
    

    def setup(self, storage):
        '''get the lines from storage'''

        self.lines = storage.get_lines()


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