import unittest

from euler import prime


class PrimeTest(unittest.TestCase):
    def test_prime_factors(self):
        self.assertListEqual([1], prime.prime_factors(1))
        self.assertListEqual([2], prime.prime_factors(2))
        self.assertListEqual([2, 3], prime.prime_factors(6))
        self.assertListEqual([2, 2], prime.prime_factors(4))
        self.assertListEqual([2, 2, 2, 5, 5], prime.prime_factors(200))

    def test_generate_primes(self):
        pass

    def test_n_primes(self):
        def as_list(seq):
            return [i for i in seq]

        self.assertListEqual([2], as_list(prime.n_primes(1)))
        self.assertListEqual([2, 3, 5, 7], as_list(prime.n_primes(4)))
        self.assertListEqual(
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
                101,
                103,
                107,
                109,
                113,
                127,
                131,
                137,
                139,
                149,
                151,
                157,
                163,
                167,
                173,
                179,
                181,
                191,
                193,
                197,
                199,
                211,
                223,
                227,
                229,
                233,
                239,
                241,
                251,
                257,
                263,
                269,
                271,
                277,
                281,
                283,
                293,
                307,
                311,
                313,
                317,
                331,
                337,
                347,
                349,
                353,
                359,
                367,
                373,
                379,
                383,
                389,
                397,
                401,
                409,
                419,
                421,
                431,
                433,
                439,
                443,
                449,
                457,
                461,
                463,
                467,
                479,
                487,
                491,
                499,
                503,
                509,
                521,
                523,
                541,
            ],
            as_list(prime.n_primes(100)),
        )

    def test_nth_prime(self):
        self.assertEqual(2, prime.nth_prime(1))
        self.assertEqual(7, prime.nth_prime(4))
        self.assertEqual(541, prime.nth_prime(100))
