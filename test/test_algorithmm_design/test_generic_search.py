import unittest

from algorithm_design.generic_search import linear_contains, binary_contains


class TestGenericSearch(unittest.TestCase):

    def test_linear_search(self):
        is_contained = linear_contains([1, 5, 15, 15, 15, 15, 20], 5)
        self.assertTrue(is_contained)

    def test_binary_search(self):
        is_contained = binary_contains(["a", "d", "e", "f", "z"], "f")
        self.assertTrue(is_contained)

        is_contained = binary_contains(["john", "mark", "ronald", "sarah"], "sheila")
        self.assertTrue(not is_contained)


if __name__ == '__main__':
    unittest.main()
