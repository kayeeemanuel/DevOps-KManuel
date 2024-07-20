# test_hello.py
import unittest
from hello import hello_function

class TestHelloFunction(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_function(), "Hello, World!")

    def test_feature_x(self):
        self.assertEqual(hello_function('Feature X'), "Feature X")

    def test_feature_y(self):
        self.assertEqual(hello_function('Feature Y'), "Feature Y")

    def test_fail_case_1(self):
        self.assertEqual(hello_function('Fail 1'), "This should fail")

    def test_fail_case_2(self):
        self.assertEqual(hello_function('Fail 2'), "This should also fail")

if __name__ == '__main__':
    unittest.main()
