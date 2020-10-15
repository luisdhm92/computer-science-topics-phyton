import unittest

from string_matching.boyer_moore import BoyerMoore
from string_matching.brute_force_match import BruteForceMatch
from string_matching.kmp import KMP


class TestStringMatching(unittest.TestCase):

    def setUp(self):
        self.target: str = "Lorem ipsum dolor"
        self.substring1: str = "Lorem"
        self.substring2: str = "Hipsum"

    def test_brute_force(self):
        match1: int = BruteForceMatch.find(self.target, self.substring1)
        match2: int = BruteForceMatch.find(self.target, self.substring2)

        self.assertEqual(match1, 0)
        self.assertEqual(match2, -1)

    def test_boyer_more(self):
        match1: int = BoyerMoore.find(self.target, self.substring1)
        match2: int = BoyerMoore.find(self.target, self.substring2)

        self.assertEqual(match1, 0)
        self.assertEqual(match2, -1)

    def test_kmp(self):
        match1: int = KMP.find(self.target, self.substring1)
        match2: int = KMP.find(self.target, self.substring2)

        self.assertEqual(match1, 0)
        self.assertEqual(match2, -1)


if __name__ == '__main__':
    unittest.main()
