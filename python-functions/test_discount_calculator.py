from unittest import TestCase

from discount_calculator import *

class Discount_Calculator_App(TestCase):
    
    def test_that_function_exists(self):
        self.assertTrue(callable(ten_off_discount))
        self.assertTrue(callable(fifty_off_discount))
        
    def test_that_ten_off_function_calculates_at_ten_percent(self):
        actual = ten_off_discount(200000)
        expected = 18000
        self.assertAlmostEqual(actual, expected)
