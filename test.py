import unittest
from lib import *

def main():
    unittest.main()

class Test(unittest.TestCase):
    def test_sum_up(self):
        self.assertEqual(sum_up_to(10), 55, "Sum up 10 works")
        self.assertEqual(sum_up_to(100), 5050, "Sum up 100 works")

    def test_sum_even(self):
        self.assertAlmostEqual(sum_even(10), 30, "Sum up even works")

    def test_sum_between(self):
        self.assertEqual(sum_between(0, 10), 55, "Sum between works")
        self.assertEqual(sum_between(5, 10), 45)
        self.assertEqual(sum_between(-5, 6), 6)

    def test_factorial(self):
      self.assertEqual(factorial(11), 39916800, "Factorial works")
      self.assertEqual(factorial(0), 1, "Factorial works")
      self.assertEqual(factorial(7), 5040, "Factorial works")

    def test_double_factorial(self):
      self.assertEqual(double_factorial(11), 10395, "double factorial works")
      self.assertEqual(double_factorial(0), 1, "double factorial works")
      self.assertEqual(double_factorial(7), 105, "Double factorial works")
      self.assertEqual(double_factorial(15), 2027025, "Double factorial works")

    def test_gcd(self):
        self.assertEqual(gcd(2,4), 2, "GCD works")

    #def test_multiples(self):
        #print_multiples()
        #print_multiples_general(10, 100)

    def test_divisors(self):
        self.assertEqual(count_divisors(12), 6)
        self.assertEqual(count_divisors(14), 4)
        self.assertEqual(count_divisors(17), 2)
        self.assertEqual(count_divisors(25), 3)
        self.assertEqual(count_divisors(24), 8)
        self.assertEqual(count_divisors(10), 4)

    def test_count(self):
        test = [2, 2, "fisk", "kage", 4, 69, 2]
        self.assertEqual(count(2, test), 3)

    def test_subset(self):
      w = [2, 2, "fisk", "kage", 4, 69, 2]
      self.assertEqual(subset([2, "fisk"], w), True)


if __name__ == "__main__":
    unittest.main()
