import unittest
from typing import List

from sorting.merge_sort import MergeSort


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.target: List[int] = [7, 8, 2, 25, 4, 7]

    def test_merge_sort(self):
        print(self.target)
        MergeSort.merge_sort(self.target)
        print(self.target)
        for index in range(0, self.target.__len__() - 1):
            self.assertTrue(self.target[index] <= self.target[index + 1])



if __name__ == '__main__':
    unittest.main()
