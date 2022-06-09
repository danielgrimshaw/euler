import unittest

from euler import restrictions


class RestrictionsTest(unittest.TestCase):
    def test_constrain_int(self):
        bad_values = ["test", b"test", 2.3, object()]
        for value in bad_values:
            print(value)
            self.assertRaisesRegex(
                ValueError,
                "%s is not an integer" % type(value),
                lambda: restrictions._constrain_int(value),
            )

        restrictions._constrain_int(-1_000_000_000)
        restrictions._constrain_int(-1)
        restrictions._constrain_int(0)
        restrictions._constrain_int(1)
        restrictions._constrain_int(1_000_000_000)

    def test_constrain_positive_int(self):
        self.assertRaisesRegex(
            ValueError,
            r"-1 is not positive$",
            lambda: restrictions._constrain_positive_int(-1),
        )
        self.assertRaisesRegex(
            ValueError,
            r"-1 is not positive or zero",
            lambda: restrictions._constrain_positive_int(-1, allow_zero=True),
        )
        self.assertRaisesRegex(
            ValueError,
            r"0 is not positive$",
            lambda: restrictions._constrain_positive_int(0),
        )
        restrictions._constrain_positive_int(0, allow_zero=True)
        restrictions._constrain_positive_int(1)
        restrictions._constrain_positive_int(1_000_000_000)

    def test_constrain_positive_wrapper(self):
        @restrictions.constrain_positive
        def wrapped(n):
            return n

        self.assertRaisesRegex(
            ValueError,
            r"-1 is not positive$",
            lambda: wrapped(-1),
        )
        self.assertRaisesRegex(
            ValueError,
            r"0 is not positive$",
            lambda: wrapped(0),
        )

        self.assertEqual(1, wrapped(1))
        self.assertEqual(1_000_000_000, wrapped(1_000_000_000))

    def test_constrain_positive_or_zero_wrapper(self):
        @restrictions.constrain_positive_or_zero
        def wrapped(n):
            return n

        self.assertRaisesRegex(
            ValueError,
            r"-1 is not positive or zero$",
            lambda: wrapped(-1),
        )
        self.assertEqual(0, wrapped(0))
        self.assertEqual(1, wrapped(1))
        self.assertEqual(1_000_000_000, wrapped(1_000_000_000))
