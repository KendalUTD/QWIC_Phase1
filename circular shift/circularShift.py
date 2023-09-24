

class CircularShift:

    lines = []
    circular_shifted_lines = []

    def __init__(self, lines):
        """this acts as the setup method in the diagram"""

        self.lines = lines
        '''starting the circular shift'''
        self.__circular_shifts()

    def add_lines(self, line):
        self.lines = line
    
    def get_lines(self):
        
        return self.lines
    
    def __circular_shift(self, line):
        '''shifts every word in a single line'''
        words = line.split()
        temp_words = words
        for _ in range(len(words)):
            
            temp_words = [temp_words[-1]] + temp_words[:-1]
            shifted_line = ' '.join(temp_words)
            self.circular_shifted_lines.append(shifted_line)

    def __circular_shifts(self):
        '''invokes circular shift for every line in the lines'''
    
        for line in self.lines:
            self.__circular_shift(line)

    def get_shifted_lines(self):
        return self.circular_shifted_lines