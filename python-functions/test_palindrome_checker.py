from unittest import TestCase
from palindrome_checker import *

class Palindrome_Palindrome_App(TestCase):
    
    def test_that_function_actually_exists(self):
        self.assertTrue(callable(is_palindrome))
        self.assertTrue(callable(is_prime_number))
        
    def test_that_function_reverses_number(self):
        actual = is_palindrome(1234)
        expected = 4321
        self.assertEqual(actual, expected)
           
    def test_that_number_user_enters_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        
    def test_that_number_is_prime_number(self):
        self.assertTrue(is_prime_number(3))
