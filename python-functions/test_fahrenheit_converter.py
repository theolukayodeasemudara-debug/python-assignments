from unittest import TestCase
from fahrenheit_converter import fah_converter, cel_converter

class Fahrenheit_Converter_Test_App(TestCase):

    def test_that_function_exists(self):
        self.assertTrue(callable(fah_converter))
        self.assertTrue(callable(cel_converter))
        
    def test_that_function_converts_to_celsius(self):
        actual = cel_converter(20)
        expected = -6.67
        self.assertAlmostEqual(actual, expected, places=2)
        
    def test_that_function_converts_to_fahrenheit(self):
        actual = fah_converter(0)
        expected = 32.0
        self.assertAlmostEqual(actual, expected, places=2)
