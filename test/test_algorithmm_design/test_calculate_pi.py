import unittest

from algorithm_design.calculate_pi import calculate_pi


class TestCalculatePi(unittest.TestCase):

    def test_fibonacci(self):
        delta: float = 0.0001
        pi = calculate_pi(1000000)

        self.assertTrue(abs(pi - 3.14159) < delta)


if __name__ == '__main__':
    unittest.main()
