"""This module represents the alphabetic shift component of the kwic system."""

class AlphabeticShift:
    def __init__(self, circular_shifter):
        self.circular_shifter = circular_shifter
        self.sorted_shifted_lines = []

    def setup(self):
        self.csLines = self.circular_shifter.get_lines()
        self.url = self.storage.get_url()
        self.page_lines = []
        self.__alpha()

    def __alpha(self):
        '''get the sorted list of shifted lines from db and merge sort them with new lines'''
        db_lines = get_from_dB()  # [{url: [lines]}]
        self.csLines = self._sort_lines(self.csLines)   
        self.page_lines = self._create_dict(self.csLines)
        self.sorted_shifted_lines = self.__merge_sort(self.page_lines, db_lines)

    def _get_from_dB(self):
        '''get the sorted list of shifted lines from db   ==>  {url: [lines]}'''
        #TODO
        pass


    def _sort_lines(self, lines):
        """Sorts the alphabetically."""
        lines.sort()
        return lines
    
    def _create_dict(self, lines):
        '''create a dictionary with sorted lines as keys and lines as values'''
        dict_lines = []
        for line in lines:
            dict_lines.append({self.url: line})
        return dict_lines
        

    # def __merge_sort(self, lines):
    #     if len(lines) <= 1:
    #         return lines

    #     # Split the list in half
    #     mid = len(lines) // 2
    #     left_half = lines[:mid]
    #     right_half = lines[mid:]

    #     # Recursively merge sort both halves
    #     left_half = self.__merge_sort(left_half)
    #     right_half = self.__merge_sort(right_half)

    #     # Merge the sorted halves
    #     sorted_lines = []
    #     left_index, right_index = 0, 0

    #     while left_index < len(left_half) and right_index < len(right_half):
    #         if left_half[left_index].lower() < right_half[right_index].lower():
    #             sorted_lines.append(left_half[left_index])
    #             left_index += 1
    #         else:
    #             sorted_lines.append(right_half[right_index])
    #             right_index += 1

    #     sorted_lines.extend(left_half[left_index:])
    #     sorted_lines.extend(right_half[right_index:])
    #     return sorted_lines

    def get_lines(self):
        return self.sorted_shifted_lines


    def __merge_sort(self, linesA, linesB=None):
        '''merge sort 2 dictionary with sorted lists and case sensitive ==> [{url: [lines]}]'''

        if linesB == None:
            linesB = []
        sorted_lines = []
        i = 0
        j = 0
        while i < len(linesA) and j < len(linesB):

            lines_listA = list(linesA[i].values())[0]
            lines_listB = list(linesB[j].values())[0]

            if lines_listA < lines_listB:
                sorted_lines.append(linesA[i])
                i += 1
            else:
                sorted_lines.append(linesB[j])
                j += 1
        sorted_lines += linesA[i:]
        sorted_lines += linesB[j:]
        return sorted_lines
        
        

