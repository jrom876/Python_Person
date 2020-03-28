
Couldn't help yourself, huh?

See: https://realpython.com/python-testing/#automated-vs-manual-testing

This is the basic setup for unittest:

from my_sum import sum
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

In a separate file, create the following:

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
#############################################

Method 	                  Equivalent to
.assertEqual(a, b) 	      a == b
.assertTrue(x) 	          bool(x) is True
.assertFalse(x) 	        bool(x) is False
.assertIs(a, b) 	        a is b
.assertIsNone(x) 	        x is None
.assertIn(a, b) 	        a in b
.assertIsInstance(a, b) 	isinstance(a, b)
