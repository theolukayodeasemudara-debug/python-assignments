from unittest import TestCase

import discount_calculator

class Discount_Calculator_App(TestCase):
    
    def test_that_function_exists(self):
        self.assertTrue(callable(discount_calculator.ten_off_discount))
        self.assertTrue(callable(discount_calculator.fifty_off_discount))
        
    def test_that_ten_off_function_calculates_at_ten_percent(self):
        actual = discount_calculator.ten_off_discount(20000)
        expected = 2000.00
        self.assertAlmostEqual(actual, expected, places = 2)
        
    def test_that_ten_off_function_calculates_at_50_percent(self):
        actual = discount_calculator.fifty_off_discount(20000)
        expected = 10000
        self.assertAlmostEqual(actual, expected, places = 2)
