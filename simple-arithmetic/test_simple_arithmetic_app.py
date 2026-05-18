from unittest import Testcase

import simple_arithmetic_app

class Test_Simple_Arithmetic_App(TestCase):

    def generate_random_number(self):
        self.assertTrue(callable(simple_arithmetic_app.random_num()))
