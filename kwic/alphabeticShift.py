"""This module represents the alphabetic shift component of the kwic system."""

import sqlite3

conn = sqlite3.connect('kwic.db')
cursor = conn.cursor()

class AlphabeticShift:
    def __init__(self, circular_shifter, storage):
        self.circular_shifter = circular_shifter
        self.storage = storage
        self.sorted_shifted_lines = []

    def setup(self):
        self.csLines = self.circular_shifter.get_lines()
        self.url = self.storage.get_url()
        self.page_lines = []
        self.__alpha()

    def __alpha(self):
        '''get the sorted list of shifted lines from db and merge sort them with new lines'''
        db_lines = self._get_from_dB()  # [(url, line)]
        self.csLines = self._sort_lines(self.csLines)   
        self.page_lines = self._create_tuple(self.csLines)
        self.sorted_shifted_lines = self.__merge_sort(self.page_lines, db_lines)

    def _get_from_dB(self):
        '''get the sorted list of shifted lines from db   ==>  {url: [lines]}'''
        
        cursor.execute("SELECT * FROM kwic")
        db_lines = cursor.fetchall()
        return db_lines
        

    def _sort_lines(self, lines):
        """Sorts the alphabetically."""
        lines.sort()
        return lines
    
    def _create_tuple(self, lines):
        '''create a dictionary with sorted lines as keys and lines as values'''
        tuple_lines = []
        for line in lines:
            tuple_lines.append((self.url, line))
        return tuple_lines
        

    def get_lines(self):
        return self.sorted_shifted_lines


    def __merge_sort(self, linesA, linesB=None):
        '''merge sort 2 tuples with sorted lists and case sensitive ==> [(url, line)]'''

        if linesB == None:
            linesB = []
        sorted_lines = []
        i = 0
        j = 0
        while i < len(linesA) and j < len(linesB):

            lines_listA = linesA[i][1]
            lines_listB = linesB[j][1]

            if lines_listA < lines_listB:
                sorted_lines.append(linesA[i])
                i += 1
            else:
                sorted_lines.append(linesB[j])
                j += 1
        sorted_lines += linesA[i:]
        sorted_lines += linesB[j:]
        return sorted_lines
        
        

