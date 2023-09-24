from kwic.storage import LineStorage
import unittest
from random import randint


class TestStorage(unittest.TestCase):

    def test_empty_storage(self):
        lstg = LineStorage()

        for i in range(100):
            self.assertEqual(lstg.char(randint(0, 100), randint(0, 100), randint(0, 100)), None)
            self.assertEqual(lstg.word(randint(0, 100)), 0)

    def test_single_line_stores_correctly(self):
        line = "Songs but chief has ham widow downs"
        lstg = LineStorage()

        # store it
        for w,word in enumerate(line.split(), 1):
            for c,char in enumerate(word, 1):
                lstg.set_char(1, w, c, char)

        # verify it
        self.assertEqual(lstg.char(1, 1, 1), 'S')
        self.assertEqual(lstg.char(1, 1, 2), 'o')
        self.assertEqual(lstg.char(1, 1, 3), 'n')
        self.assertEqual(lstg.char(1, 1, 4), 'g')
        self.assertEqual(lstg.char(1, 1, 5), 's')

        self.assertEqual(lstg.char(1, 2, 1), 'b')
        self.assertEqual(lstg.char(1, 2, 2), 'u')
        self.assertEqual(lstg.char(1, 2, 3), 't')

        self.assertEqual(lstg.char(1, 3, 1), 'c')
        self.assertEqual(lstg.char(1, 3, 2), 'h')
        self.assertEqual(lstg.char(1, 3, 3), 'i')
        self.assertEqual(lstg.char(1, 3, 4), 'e')
        self.assertEqual(lstg.char(1, 3, 5), 'f')

        self.assertEqual(lstg.char(1, 4, 1), 'h')
        self.assertEqual(lstg.char(1, 4, 2), 'a')
        self.assertEqual(lstg.char(1, 4, 3), 's')

        self.assertEqual(lstg.char(1, 5, 1), 'h')
        self.assertEqual(lstg.char(1, 5, 2), 'a')
        self.assertEqual(lstg.char(1, 5, 3), 'm')

        self.assertEqual(lstg.char(1, 6, 1), 'w')
        self.assertEqual(lstg.char(1, 6, 2), 'i')
        self.assertEqual(lstg.char(1, 6, 3), 'd')
        self.assertEqual(lstg.char(1, 6, 4), 'o')
        self.assertEqual(lstg.char(1, 6, 5), 'w')

        self.assertEqual(lstg.char(1, 7, 1), 'd')
        self.assertEqual(lstg.char(1, 7, 2), 'o')
        self.assertEqual(lstg.char(1, 7, 3), 'w')
        self.assertEqual(lstg.char(1, 7, 4), 'n')
        self.assertEqual(lstg.char(1, 7, 5), 's')

        self.assertEqual(lstg.word(1), 7)

    def test_single_line_error_returns(self):
        line = "Songs but chief has ham widow downs"
        lstg = LineStorage()

        # test <= 0
        self.assertEquals(lstg.word(1), 0)
        lstg.set_char(0, 1, 1, 0)
        lstg.set_char(1, 0, 1, 1)
        lstg.set_char(1, 1, 0, 1)
        lstg.set_char(-1, 1, 1, 1)
        lstg.set_char(1, -1, 1, 1)
        lstg.set_char(1, 1, -1, 1)
        self.assertEquals(lstg.word(1), 0)

        # store it
        for w,word in enumerate(line.split(), 1):
            for c,char in enumerate(word, 1):
                lstg.set_char(1, w, c, char)

        # test char
        for i in range(100):
            r1, r2, r3 = randint(-100, 100), randint(-100, 100), randint(-100, 100)
            while r1 == 1:
                r1 = randint(-100, 100)
            while r2 == 1:
                r2 = randint(-100, 100)
            while r3 == 1:
                r3 = randint(-100, 100)

            self.assertEqual(lstg.char(r1, r2, r3), None)

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
            for w,word in enumerate(line.split(), 1):
                for c,char in enumerate(word, 1):
                    lstg.set_char(l, w, c, char)

        # verify it
        self.assertEqual(lstg.char(1, 1, 1), 'G')
        self.assertEqual(lstg.char(1, 1, 2), 'e')
        self.assertEqual(lstg.char(1, 1, 3), 'n')
        self.assertEqual(lstg.char(1, 1, 4), 'i')
        self.assertEqual(lstg.char(1, 1, 5), 'u')
        self.assertEqual(lstg.char(1, 1, 6), 's')

        self.assertEqual(lstg.char(2, 1, 1), 'L')
        self.assertEqual(lstg.char(2, 1, 2), 'a')
        self.assertEqual(lstg.char(2, 1, 3), 'r')
        self.assertEqual(lstg.char(2, 1, 4), 'g')
        self.assertEqual(lstg.char(2, 1, 5), 'e')

        self.assertEqual(lstg.char(2, 2, 1), 'd')
        self.assertEqual(lstg.char(2, 2, 2), 'o')

        self.assertEqual(lstg.char(2, 3, 1), 't')
        self.assertEqual(lstg.char(2, 3, 2), 'r')
        self.assertEqual(lstg.char(2, 3, 3), 'i')
        self.assertEqual(lstg.char(2, 3, 4), 'e')
        self.assertEqual(lstg.char(2, 3, 5), 'd')

        self.assertEqual(lstg.char(3, 1, 1), 'S')
        self.assertEqual(lstg.char(3, 1, 2), 'i')
        self.assertEqual(lstg.char(3, 1, 3), 'l')
        self.assertEqual(lstg.char(3, 1, 4), 'e')
        self.assertEqual(lstg.char(3, 1, 5), 'n')
        self.assertEqual(lstg.char(3, 1, 6), 't')

        self.assertEqual(lstg.word(1), 6)
        self.assertEqual(lstg.word(2), 7)
        self.assertEqual(lstg.word(3), 9)
        self.assertEqual(lstg.word(4), 8)