import unittest

from euler import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_nth_fib(self):
        self.assertEqual(1, fibonacci.nth_fib(1))
        self.assertEqual(1, fibonacci.nth_fib(2))
        self.assertEqual(2, fibonacci.nth_fib(3))
        self.assertEqual(3, fibonacci.nth_fib(4))
        self.assertEqual(5, fibonacci.nth_fib(5))
        self.assertEqual(354_224_848_179_261_915_075, fibonacci.nth_fib(100))

    def test_fibonacci(self):
        for i, n in enumerate(fibonacci.fibonacci()):
            if i > 100:
                break
            self.assertEqual(fibonacci.nth_fib(i + 1), n)

    def test_n_fibonacci(self):
        def as_list(seq):
            return [n for n in seq]

        self.assertListEqual([1], as_list(fibonacci.n_fibonacci(1)))
        self.assertListEqual([1, 1, 2, 3, 5, 8, 13], as_list(fibonacci.n_fibonacci(7)))
