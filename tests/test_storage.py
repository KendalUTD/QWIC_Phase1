from kwic.storage import LineStorage
import unittest
from random import randint


class TestStorage(unittest.TestCase):

    def test_empty_storage(self):
        lstg = LineStorage()

        for i in range(100):
            self.assertEqual(lstg.get_line(randint(0, 100)), None)
            self.assertEqual(lstg.word(randint(0, 100)), 0)

    def test_single_line_stores_correctly(self):
        line = "Songs but chief has ham widow downs"
        lstg = LineStorage()

        lstg.set_line(1, line)

        self.assertEqual(lstg.get_line(1), line)
        self.assertEqual(lstg.word(1), 7)

    def test_single_line_error_returns(self):
        line = "Songs but chief has ham widow downs"
        lstg = LineStorage()

        # test <= 0
        self.assertEqual(lstg.word(1), 0)
        lstg.set_line(0, 1)
        lstg.set_line(-1, 1)
        self.assertEqual(lstg.word(1), 0)

        # store it
        lstg.set_line(1, line)

        # test line
        for i in range(100):
            r1 = randint(-100, 100)
            while r1 == 1:
                r1 = randint(-100, 100)
            self.assertEqual(lstg.get_line(r1), None)

        # test word
        for i in range(100):
            r1 = randint(-100, 100)
            while r1 == 1:
                r1 = randint(-100, 100)
            self.assertEqual(lstg.word(r1), 0)

    def test_multiple_lines_store_correctly(self):
        lines = [
            "Genius or so up vanity cannot",
            "Large do tried going about water defer",
            "Silent son man she wished mother go outside to",
            "Distrusts allowance do knowledge eagerness assurance additions to"
        ]
        lstg = LineStorage()

        # store it
        for l,line in enumerate(lines, 1):
            lstg.set_line(l, line)

        # verify it
        self.assertEqual(lstg.get_line(1), lines[0])
        self.assertEqual(lstg.get_line(2), lines[1])
        self.assertEqual(lstg.get_line(3), lines[2])
        self.assertEqual(lstg.get_line(4), lines[3])