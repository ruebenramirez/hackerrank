import unittest
from binary_numbers import count_binary_ones


class ConsecutiveOneCountInBaseTenRepresentation(unittest.TestCase):

    def test_count_ones_in_binary_of_0(self):
        self.assertEqual(count_binary_ones(0), 0)

    def test_count_ones_in_binary_of_5(self):
        self.assertEqual(count_binary_ones(5), 1)

    def test_count_ones_in_binary_of_13(self):
        self.assertEqual(count_binary_ones(13), 2)


if __name__ == '__main__':
    unittest.main()
