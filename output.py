class Output:
    def __init__(self, alpha_shifter):
        self.alpha_shifter = alpha_shifter

    def display(self):
        sorted_lines = self.alpha_shifter.get_sorted_lines()
        for line in sorted_lines:
            print(line)
