import unittest

from algorithm_design.fibonacci import recursive_fibonacci, fibonacci


class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci(self):
        fib_iter = 0
        fib_rec = recursive_fibonacci(50)
        print(f"fib_rec {fib_rec}")
        for i in fibonacci(50):
            fib_iter = i

        print(f"fib_iter {fib_iter}")

        self.assertEqual(fib_iter, fib_rec, "Both results should have the same value")


if __name__ == '__main__':
    unittest.main()
