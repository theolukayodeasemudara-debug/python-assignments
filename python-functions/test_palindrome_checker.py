from unittest import TestCase
import palindrome_checker

class Palindrome_Palindrome_App(TestCase):
    
    def test_that_function_actually_exists(self):
        self.assertTrue(callable(palindrome_checker.is_palindrome))
        self.assertTrue(callable(palindrome_checker.is_prime_number))
        
    def test_that_function_reverses_number(self):
        actual = palindrome_checker.is_palindrome(1234)
        expected = 4321
        self.assertEqual(actual, expected)
           
    def test_that_number_user_enters_is_palindrome(self):
        self.assertTrue(palindrome_checker.is_palindrome(121))
        
    def test_that_number_is_prime_number(self):
        self.assertTrue(palindrome_checker.is_prime_number(3))
