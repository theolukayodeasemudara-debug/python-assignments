from unittest import TestCase

from palindrome_checker import *

class Palindrome_Palindrome_App(TestCase):
    
    def test_that_function_actually_exists(self):
        self.assertTrue(callable(is_palindrome))
        
    def test_that_number_user_enters_is_palindrome(self):
        actual = is_palindrome(1234)
        expected = 4321
        self.assertEqual(actual, expected)
