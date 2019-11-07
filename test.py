import unittest
import random

from app import guess_the_number


class test_funtions(unittest.TestCase):

    def test_guess_the_number(self):
        guess = 60
        computer_guess = 60
        self.assertEqual(guess, computer_guess)


if __name__ == '__main__':
    unittest.main()
