import unittest

from algorithm_design.hanoi import Stack, hanoi


class TestHanoi(unittest.TestCase):

    def setUp(self):
        self.num_discs: int = 3
        self.tower_a: Stack[int] = Stack()
        self.tower_b: Stack[int] = Stack()
        self.tower_c: Stack[int] = Stack()
        for i in range(1, self.num_discs + 1):
            self.tower_a.push(i)

    def test_fibonacci(self):
        print(f"{self.tower_a} {self.tower_b} {self.tower_c}")
        hanoi(self.tower_a, self.tower_c, self.tower_b, self.num_discs)
        print(f"{self.tower_a} {self.tower_b} {self.tower_c}")

        self.assertTrue(self.tower_a.empty)
        self.assertTrue(self.tower_c.__len__() == 3)


if __name__ == '__main__':
    unittest.main()
